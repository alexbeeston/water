def getNumberCorrect(classifications, labels):
    pass

def splitData(fold, data):
    pass  # return training and validation sets


EPOCHS = 10
FOLDS = 5

data = []
trainingAccuraciesByFold = []
validationAccuraciesByFold = []

for fold in range(FOLDS):
    print(f'Fold {fold + 1}')
    classifier = 10
    trainingLoader, validationLoader = splitData(fold, data)
    optimizer = 10
    criteria = 10
    trainingAccuracies = []
    validationAccuracies = []
    classifier.train()
    for epoch in range(EPOCHS):
        print(f'   Epoch {epoch + 1}')
        # training
        correct = 0
        for labelBatch, imageBatch in trainingLoader:
            classifications = classifier(imageBatch)
            optimizer.zero_grad()
            loss = criteria(classifications, labelBatch)
            loss.backwards()
            optimizer.step()
            correct += getNumberCorrect(classifications, labelBatch)
        trainingAccuracy = correct * 100 / len(trainingLoader.data)
        trainingAccuracies.append(trainingAccuracy)
        print(f'      Training Accuracy: {round(trainingAccuracy, 2)}%')

        # validation
        correct = 0
        with torch.no_grad():
            for labelBatch, imageBatch in validationLoader:
                # with no gradient (?)
                classifications = classifier(imageBatch)
                correct += getNumberCorrect(classifications, labelBatch)
        validationAccuracy = correct * 100 / len(validationLoader.data)
        validationAccuracies.append(trainingAccuracy)
        print(f'      Validation Accuracy: {round(validationAccuracy, 2)}%')

        # save state? Look at HW 4


    trainingAccuraciesByFold.append(trainingAccuracies)
    validationAccuraciesByFold.append(validationAccuracies)

