from PIL import Image
import os


def getImages():
	originalImages = []
	for originalFile in os.listdir():
		if originalFile.endswith('.jpg'):
			originalImages.append(originalFile)
	return originalImages


def getNewFileName(oldName, key):
	return oldName.split('.')[0] + '_' + key + '.jpg'


def applyTransformations(transformations):
	for imageFile in getImages():
		image = Image.open(imageFile)
		for key in transformations.keys():
			temp = image.transpose(transformations[key])
			fileName = getNewFileName(imageFile, key)
			temp.save(fileName)

		
def applyTints(tints):
	for imageFile in getImages():
		image = Image.open(imageFile)
		for key in tints.keys():
			tint = Image.new('RGB', image.size, color=tints[key])
			tintFactor = .5
			temp = Image.blend(image, tint, tintFactor)
			fileName = getNewFileName(imageFile, key)
			temp.save(fileName)


rotations = {
	'_rot90': Image.ROTATE_90,
	'_rot180': Image.ROTATE_180,
	'_rot270': Image.ROTATE_270
	}
applyTransformations(rotations)



flips = {
	'_flip': Image.FLIP_LEFT_RIGHT
	}
applyTransformations(flips)



tints = {
	'_red': 'red',
	'_blue': 'blue',
	'_green': 'green'
	}
applyTints(tints)
