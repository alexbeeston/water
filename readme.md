## Glass of Water
_ Group Members: Alex Beeston, Malachi Harper, & Kaleb Lott
_ Group Project Manager: Alex Beeston
_ Topic of Research: Simulation of robotic manipulators (fixed or mobile) that make decisions using computer vision; could be applied to manufacturing, surgery, and social robotics

## Description
This program first classifies images of concrete based on whether or not they are cracked. Images of concrete, both cracked and intact, are in data/croppedImages/cracked and data/croppedImage/intact, respectively. The program src/main.py classifies these images using the ResNet18 neural network with 5-fold cross validation. With the default configurations (located in src/configurations.py), each of the five folds took about 20 minutes running on a CPU on Ubuntu 20.04. The program prints out the training and validation accuracies of the classifier after each epoch of each fold. The classifier achieves >80% accuracy on the validation sets.

## Instructions
1. If pipenv is not installed, install pipenv. On Windows (and probably Linux), should be just `pip install pipenv`.
2. Create the virtual environment with `pipenv install`.
3. Activate virtual environment with `pipenv shell`.
4. Run the classifier as `python3 src/main.py dir/to/positive/samples dir/to/negative/samples`. For example, to classify the sample images, run `python3 src/main.py data/croppedImages/cracked data/croppedImages/intact`.
5. Observe or redirect the console output to a log file.

To do:
1. programatically visualize results
2. deepcopy the network after new best accuracies are met
3. provide function to classify a single image using the copied model saved to disk from (1)
4. employ image transformations at the DataSet layer
5. convert to a GPU notebook
6. figure out how to run the GPU notebook on Google Colab for performance increase
