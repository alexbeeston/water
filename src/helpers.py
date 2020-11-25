import os
from configurations import hyperParams
import torch
from torch.utils.data import DataLoader

def buildListOfPaths(dir):
    return [
        os.path.join(dir, fileName)
        for fileName in os.listdir(dir)
    ]

def getBatchSize(dataSet):
    size = int(hyperParams['batchSizeFactor'] * len(dataSet))
    if size < 1:
        return 1
    else:
        return size


def getDataLoader(dataset):
    batchSize = getBatchSize(dataset)
    return DataLoader(
        dataset,
        batch_size=batchSize,
        shuffle=True,
        num_workers=hyperParams['numWorkers']
    )


def countCorrects(softmax, labels):
    classifications = torch.argmax(softmax, dim=1)
    assert classifications.shape == labels.shape, 'shapes do not match'
    valuesMatch = (classifications == labels)
    return valuesMatch.sum().item()


def train(model, optimizer, criteria, trainLoader, valLoader, numTrain, numVal):
    trainAccuracies = []
    valAccuracies = []
    for epoch in range(hyperParams['epochs']):
        print(f'   Epoch {epoch + 1}:')
        # ****** Training *******
        correct = 0
        model.train()
        for images, labels in trainLoader:
            optimizer.zero_grad()
            classifications = model(images)
            loss = criteria(classifications, labels)
            loss.backward()
            optimizer.step()
            correct += countCorrects(classifications, labels)
        trainAccuracy = correct * 100 / numTrain
        trainAccuracies.append(trainAccuracy)
        print(f'      Training Accuracy: {round(trainAccuracy, 2)}%')

        # ****** Validation *******
        correct = 0
        model.eval()
        with torch.no_grad():
            for images, labels in valLoader:
                optimizer.zero_grad()
                classifications = model(images)
                correct += countCorrects(classifications, labels)
            valAccuracy = correct * 100 / numVal
            valAccuracies.append(valAccuracy)
            print(f'      Validation Accuracy: {round(valAccuracy, 2)}%')

    return trainAccuracies, valAccuracies
