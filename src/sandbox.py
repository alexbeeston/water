# requires as input a path to directory that contains .jpg files and a csv file of form [fileName],[label]

from torch.utils.data import Dataset
import os
import sys
import csv
from PIL import Image
import torchvision.transforms as transforms

class ConcreteImages(Dataset):
    def __init__(self, pathToDir):
        pathToIndexFile = os.path.join(pathToDir, 'index.csv')
        indexFile = open(pathToIndexFile)
        self.index = []
        self.FILENAME = 0
        self.LABEL = 1
        for line in csv.reader(indexFile):
            pathToImage = os.path.join(pathToDir, line[self.FILENAME])
            label = line[self.LABEL]
            self.index.append((pathToImage, label))
        indexFile.close()

    def __len__(self):
        return len(self.index)

    def __getitem__(self, i):
        pathToImage = self.index[i][self.FILENAME]
        image = Image.open(pathToImage)
        imageConverter = transforms.ToTensor()
        tensor = imageConverter(image)
        image.close()
        return (tensor, self.index[i][self.LABEL])


if len(sys.argv) != 2:
    sys.exit('Usage: python3 sandbox.py pathToDir')

pathToDir = sys.argv[1]
concreteImages = ConcreteImages(pathToDir)
for i in range(len(concreteImages)):
    tensor = concreteImages[i]
    if i % 100 == 0:
        print(f'loaded images {i} of {len(concreteImages)}')
