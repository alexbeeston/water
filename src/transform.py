from PIL import Image
import os
from helpers import buildListOfPaths


def getNewFileName(oldName, key):
	oldName, extension = os.path.splitext(oldName)
	newName = oldName + '_' + key + extension
	return newName


def applyTransformations(transformations, dir):
	for pathToImage in buildListOfPaths(dir):
		image = Image.open(pathToImage)
		for key in transformations.keys():
			transformedImage = image.transpose(transformations[key])
			fileName = getNewFileName(pathToImage, key)
			transformedImage.save(fileName)

		
def applyTints(tints, dir):
	for pathToImage in buildListOfPaths(dir):
		image = Image.open(pathToImage)
		for key in tints.keys():
			tint = Image.new('RGB', image.size, color=tints[key])
			tintFactor = .5
			transformedImage = Image.blend(image, tint, tintFactor)
			fileName = getNewFileName(pathToImage, key)
			transformedImage.save(fileName)


def doTransforms(dir):
	rotations = {
		'_rot90': Image.ROTATE_90,
		'_rot180': Image.ROTATE_180,
		'_rot270': Image.ROTATE_270
		}
	applyTransformations(rotations, dir)
	print(f'applied rotation transformations to images in {dir}')

	flips = {
		'_flip': Image.FLIP_LEFT_RIGHT
		}
	applyTransformations(flips, dir)
	print(f'applied flip transformations to images in {dir}')

	tints = {
		'_red': 'red',
		'_blue': 'blue',
		'_green': 'green'
		}
	applyTints(tints, dir)
	print(f'applied color tinting transformations to images in {dir}')
