## Glass of Water
- Group Members: Alex Beeston, Malachi Harper, & Kaleb Lott
- Group Project Manager: Alex Beeston
- Topic of Research: Simulation of robotic manipulators that make decisions using computer vision.

## Description
This program first classifies images of concrete based on whether or not they are cracked. Images of concrete, both cracked and intact, are in data/croppedImages/cracked and data/croppedImage/intact, respectively. The program src/main.py classifies these images using the ResNet18 neural network with 5-fold cross validation. With the default configurations (located in src/configurations.py), each of the five folds took about 20 minutes running on a CPU on Ubuntu 20.04. The program prints out the training and validation accuracies of the classifier after each epoch of each fold. The classifier achieves ~94% accuracy on the validation sets.

## Instructions
1. If pipenv is not installed, install pipenv. On Windows (and probably Linux), should be just `pip install pipenv`.
2. Create the virtual environment with `pipenv install`.
3. Activate virtual environment with `pipenv shell`.
4. Run the classifier as `python3 src/main.py dir/to/positive/samples dir/to/negative/samples`. For example, to classify the sample images, run `python3 src/main.py data/croppedImages/cracked data/croppedImages/intact`.
5. Observe or redirect the console output to a log file.
