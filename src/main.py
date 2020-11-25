from transform import doTransforms
import classes
import sys
from configurations import hyperParams
from torchvision import models
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.utils.data import DataLoader

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

trainingAccuracyByFold = []
validationAccuracyByFold = []
for fold in range(hyperParams['folds']):
    print(f'Fold {fold + 1}:')
    model = models.resnet18(pretrained=True)
    lastLayerInputSize = model.fc.in_features
    model.fc = nn.Linear(lastLayerInputSize, 2)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(
        model.parameters(),
        lr=hyperParams['learningRate'],
        momentum=hyperParams['momentum']
    )
    scheduler = lr_scheduler.StepLR(
        optimizer,
        step_size=hyperParams['stepSize'],
        gamma=hyperParams['gamma']
    )
    trainingSet, validationSet = kFoldSplitter.getDataSets(fold)
    # can remove duplicate code
    trainingLoader = DataLoader(
        trainingSet,
        batch_size=int(hyperParams['batchSizeFactor'] * len(trainingSet)),
        shuffle=True,
        num_workers=hyperParams['numWorkers']
    )
    validationLoader = DataLoader(
        validationSet,
        batch_size=int(hyperParams['batchSizeFactor'] * len(validationSet)),
        shuffle=True,
        num_workers=hyperParams['numWorkers']
    )


#     trainingAccuracies = []
#     validationAccuracies = []
#     trainingData, validationData = splitData(data)
#     model.train()

    # # DRAFTED
    # for epoch in range(EPOCHS):
    #     print(f'   Epoch {epoch + 1}')
    #     # training
    #     correct = 0
    #     for labelBatch, imageBatch in trainingLoader:
    #         classifications = classifier(imageBatch)
    #         optimizer.zero_grad()
    #         loss = criteria(classifications, labelBatch)
    #         loss.backwards()
    #         optimizer.step()
    #         correct += getNumberCorrect(classifications, labelBatch)
    #     trainingAccuracy = correct * 100 / len(trainingLoader.data)
    #     trainingAccuracies.append(trainingAccuracy)
    #     print(f'      Training Accuracy: {round(trainingAccuracy, 2)}%')
    #
    #     # validation
    #     correct = 0
    #     with torch.no_grad():
    #         for labelBatch, imageBatch in validationLoader:
    #             # with no gradient (?)
    #             classifications = classifier(imageBatch)
    #             correct += getNumberCorrect(classifications, labelBatch)
    #     validationAccuracy = correct * 100 / len(validationLoader.data)
    #     validationAccuracies.append(trainingAccuracy)
    #     print(f'      Validation Accuracy: {round(validationAccuracy, 2)}%')
    #
    #     # save state? Look at HW 4
    #
    #
    # trainingAccuraciesByFold.append(trainingAccuracies)
    # validationAccuraciesByFold.append(validationAccuracies)

