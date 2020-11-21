# requires as input a path to directory that contains .jpg files and a csv file of form [fileName],[label]

from torch.utils.data import Dataset
import os
import sys
import csv

class ConcreteImages(Dataset):
    def __init__(self, pathToDir):
        self.labeledTensors = []
        pathToIndexFile = os.path.join(pathToDir, 'index.csv')
        indexFile = open(pathToIndexFile)
        FILENAME = 0
        LABEL = 1
        for line in csv.reader(indexFile):
            pathToImage = os.path.join(pathToDir, line[FILENAME])
            label = line[LABEL]
            self.labeledTensors.append((label, pathToImage))
        indexFile.close()


    def __len__(self):
        return len(self.labeledTensors)


    def __getitem__(self, index):
        return self.labeledTensors[index]


if len(sys.argv) != 2:
    sys.exit('Usage: python3 sandbox.py pathToDir')

pathToDir = sys.argv[1]
concreteImages = ConcreteImages(pathToDir)
for i in concreteImages.labeledTensors[:10]:
    print(i)
