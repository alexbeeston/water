import os
import configurations

def buildListOfPaths(dir):
    return [
        os.path.join(dir, fileName)
        for fileName in os.listdir(dir)
    ]

def countCorrectClassifications():
    pass