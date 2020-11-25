import os
from sklearn.model_selection import KFold
import helpers


# from torchvision import models
# import torch.nn as nn
# import torch.optim as optim
# from torch.utils.data import Dataset
# from PIL import Image
# import torchvision.transforms as transforms

# class ConcreteImages(Dataset):
#     def __init__(self, pathToDir):
#         pathToIndexFile = os.path.join(pathToDir, 'index.csv')
#         indexFile = open(pathToIndexFile)
#         self.index = []
#         for line in csv.reader(indexFile):
#             pathToImage = os.path.join(pathToDir, line[self.FILENAME])
#             label = line[self.LABEL]
#             self.index.append((pathToImage, label))
#         indexFile.close()
#         PRETRAINED_MEAN = [0.485, 0.456, 0.406]
#         PRETRAINED_STD = [0.229, 0.224, 2.225]
#         self.transforms = transforms.Compose([
#             transforms.ToTensor(),
#             transforms.Normalize(mean=PRETRAINED_MEAN, std=PRETRAINED_STD)
#         ])
#
#     def __len__(self):
#         return len(self.index)
#
#     def __getitem__(self, i):
#         pathToImage = self.index[i][self.FILENAME]
#         image = Image.open(pathToImage)
#         tensor = self.transforms(image)
#         image.close()
#         return (tensor, self.index[i][self.LABEL])

class KFoldSplitter:
    def __init__(self, posDir, negDir, k):
        self.posLabel = os.path.basename(posDir)
        self.negLabel = os.path.basename(negDir)
        self.pathsToPos = helpers.buildListOfPaths(posDir)
        self.pathsToNeg = helpers.buildListOfPaths(negDir)
        splitter = KFold(k)
        self.posIndices = self.__getIndicesOfFolds(self.pathsToPos, splitter)
        self.negIndices = self.__getIndicesOfFolds(self.pathsToNeg, splitter)

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
