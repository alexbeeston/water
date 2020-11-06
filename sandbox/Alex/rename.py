import os


def reNameFiles(prefix):
	counter = 1	
	for originalFileName in os.listdir():
		newFileName = prefix + '_' + str(counter) + '_crack_raw.jpg'
		os.system('cp ' + originalFileName + ' ' + newFileName)
		counter += 1


reNameFiles('A')
	
