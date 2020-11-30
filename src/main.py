from transform import doTransforms
import classes
from helpers import train, getDataLoader, getBatchSize
import sys
from configurations import hyperParams
from torchvision import models
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from numpy import mean

if len(sys.argv) < 3:
    print('Usage: python3 main.py posDir negDir [--transform]')
    sys.exit()

posDir = sys.argv[1]
negDir = sys.argv[2]
if len(sys.argv) == 4 and sys.argv[3] == '--transform':
    confirmation = input(f'Are you sure you want to apply transformations to {posDir} and {negDir}? Enter "y" for yes, or any other key for no.\n')
    if confirmation == 'y':
        doTransforms(posDir)
        doTransforms(negDir)

kFoldSplitter = classes.KFoldSplitter(posDir, negDir, hyperParams['folds'])

trainAccuracies = []
valAccuracies = []
lastTrainAccuracies = []
lastValAccuracies = []
for fold in range(hyperParams['folds']):
    model = models.resnet18(pretrained=True)
    lastLayerInputSize = model.fc.in_features
    model.fc = nn.Linear(lastLayerInputSize, 2)
    criteria = nn.CrossEntropyLoss()
    optimizer = optim.SGD(
        model.parameters(),
        lr=hyperParams['learningRate'],
        momentum=hyperParams['momentum']
    )
    scheduler = lr_scheduler.StepLR(
        optimizer,
        step_size=hyperParams['schedulerStepSize'],
        gamma=hyperParams['gamma']
    )
    trainSet, valSet = kFoldSplitter.getDataSets(fold)
    trainLoader = getDataLoader(trainSet)
    valLoader = getDataLoader(valSet)

    if fold == 0:
        print(f'** length of training set: {len(trainSet)}')
        print(f'** length of val set: {len(valSet)}')
        print(f'** training batch size: {getBatchSize(trainSet)}')
        print(f'** validation batch size: {getBatchSize(valSet)}')

    print(f'Fold {fold + 1}:')
    trainAccuracy, valAccuracy = train(
        model,
        optimizer,
        criteria,
        trainLoader,
        valLoader,
        len(trainSet),
        len(valSet)
    )
    trainAccuracies.append(trainAccuracy)
    valAccuracies.append(valAccuracy)
    lastTrainAccuracies.append(trainAccuracy[-1])
    lastValAccuracies.append(valAccuracy[-1])
    print(f'Average training accuracy after {fold + 1} folds: {round(mean(lastTrainAccuracies), 2)}%.')
    print(f'Average validation accuracy after {fold + 1} folds: {round(mean(lastValAccuracies), 2)}%.')

