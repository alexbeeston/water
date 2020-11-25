from transform import doTransforms
import classes
import sys
import configurations


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

hyperParams = configurations.hyperParams
kFoldSplitter = classes.KFoldSplitter(posDir, negDir, hyperParams['folds'])


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
