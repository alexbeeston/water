from torchvision import models
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset
import os
import sys
import csv
from PIL import Image
import torchvision.transforms as transforms
from sklearn.model_selection import KFold

def getNumberCorrect(classifications, labels):
    pass

class ConcreteImages(Dataset):
    def __init__(self, pathToDir):
        pathToIndexFile = os.path.join(pathToDir, 'index.csv')
        indexFile = open(pathToIndexFile)
        self.index = []
        for line in csv.reader(indexFile):
            pathToImage = os.path.join(pathToDir, line[self.FILENAME])
            label = line[self.LABEL]
            self.index.append((pathToImage, label))
        indexFile.close()
        PRETRAINED_MEAN = [0.485, 0.456, 0.406]
        PRETRAINED_STD = [0.229, 0.224, 2.225]
        self.transforms = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=PRETRAINED_MEAN, std=PRETRAINED_STD)
        ])

    def __len__(self):
        return len(self.index)

    def __getitem__(self, i):
        pathToImage = self.index[i][self.FILENAME]
        image = Image.open(pathToImage)
        tensor = self.transforms(image)
        image.close()
        return (tensor, self.index[i][self.LABEL])

class ValidationLoader:
    def __init__(self, posDir, negDir, k):
        self.posLabel = os.path.basename(posDir)
        self.negLabel = os.path.basename(negDir)
        self.pathsToPos = self.__buildListOfPaths(posDir)
        self.pathsToNeg = self.__buildListOfPaths(negDir)
        splitter = KFold(k)
        self.posIndices = self.__getIndicesOfFolds(self.pathsToPos, splitter)
        self.negIndices = self.__getIndicesOfFolds(self.pathsToNeg, splitter)

    def __buildListOfPaths(self, dir):
        return [
            os.path.join(dir, fileName)
            for fileName in os.listdir(dir)
        ]

    def __selectSamples(self, indices, samples, label):
        return [
            [samples[i], label]
            for i in indices
        ]

    def __getIndicesOfFolds(self, data, splitter):
        return [
            [trainingIndices, validationIndices]
            for trainingIndices, validationIndices in splitter.split(data)
        ]

    def getDataSets(self, fold):
        TRAINING = 0
        VALIDATION = 1
        posTraining = self.__selectSamples(self.posIndices[fold][TRAINING], self.pathsToPos, self.posLabel)
        posValidation = self.__selectSamples(self.posIndices[fold][VALIDATION], self.pathsToPos, self.posLabel)
        negTraining = self.__selectSamples(self.negIndices[fold][TRAINING], self.pathsToNeg, self.negLabel)
        negValidation = self.__selectSamples(self.negIndices[fold][VALIDATION], self.pathsToNeg, self.negLabel)
        return posTraining + negTraining, posValidation + negValidation


# perform transforms based on command line arg
validationLoader = ValidationLoader('../data/samples/cracked', '../data/samples/intact', 4)
print('fold 0 training:')
for i in validationLoader.getDataSets(0)[0]:
    print(i)

print('\nfold 0 validation:')
for i in validationLoader.getDataSets(0)[1]:
    print(i)

print('\n########\n')
print('fold 1 training:')
for i in validationLoader.getDataSets(1)[0]:
    print(i)

print('\nfold 1 validation:')
for i in validationLoader.getDataSets(1)[1]:
    print(i)
# # configurations
# EPOCHS = 10
# FOLDS = 5
# LEARNING_RATE = 0.001
# PATH_TO_DATA = '../../data/transformed'
#
# data = ConcreteImages(PATH_TO_DATA)
# trainingAccuraciesByFold = []
# validationAccuraciesByFold = []
# for fold in range(FOLDS):
#     print(f'Fold {fold + 1}')
#     model = models.resnet18(pretrained=True)
#     lastLayerInputSize = model.fc.in_features
#     model.fc = nn.Linear(lastLayerInputSize, 2)
#     criterion = nn.CrossEntropyLoss()
#     optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
#     scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.1)
#     trainingAccuracies = []
#     validationAccuracies = []
#     trainingData, validationData = splitData(data)
#     model.train()
#
#     # DRAFTED
#     for epoch in range(EPOCHS):
#         print(f'   Epoch {epoch + 1}')
#         # training
#         correct = 0
#         for labelBatch, imageBatch in trainingLoader:
#             classifications = classifier(imageBatch)
#             optimizer.zero_grad()
#             loss = criteria(classifications, labelBatch)
#             loss.backwards()
#             optimizer.step()
#             correct += getNumberCorrect(classifications, labelBatch)
#         trainingAccuracy = correct * 100 / len(trainingLoader.data)
#         trainingAccuracies.append(trainingAccuracy)
#         print(f'      Training Accuracy: {round(trainingAccuracy, 2)}%')
#
#         # validation
#         correct = 0
#         with torch.no_grad():
#             for labelBatch, imageBatch in validationLoader:
#                 # with no gradient (?)
#                 classifications = classifier(imageBatch)
#                 correct += getNumberCorrect(classifications, labelBatch)
#         validationAccuracy = correct * 100 / len(validationLoader.data)
#         validationAccuracies.append(trainingAccuracy)
#         print(f'      Validation Accuracy: {round(validationAccuracy, 2)}%')
#
#         # save state? Look at HW 4
#
#
#     trainingAccuraciesByFold.append(trainingAccuracies)
#     validationAccuraciesByFold.append(validationAccuracies)
#
