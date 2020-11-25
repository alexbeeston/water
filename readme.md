## Glass of Water
_ Group Members: Alex Beeston, Malachi Harper, & Kaleb Lott
_ Group Project Manager: Alex Beeston
_ Topic of Research: Simulation of robotic manipulators (fixed or mobile) that make decisions using computer vision; could be applied to manufacturing, surgery, and social robotics

## Description
This program first classifies images of concrete based on whether or not they are cracked. Images of concrete, both cracked and intact, and in data/croppedImages/cracked and data/croppedImage/intact, respectively. The program src/main.py classifies these images using the ResNet18 neural network with 5-fold cross validation. Run the program with `python3 src/main.py data/cropedImages/cracked data/croppedImages/intact`. With the default configurations (located in src/configurations.py), each of the five folds takes about 20 minutes to run on a CPU. The programs prints to the console the trainig and validation accuracies of the classifier after each epoch of each fold.

To do:
1. programatically visualize results
2. deepcopy the network after new best accuracies are met
3. provide function to classify a single image using the copied model saved to disk from (1)
4. employ image transformations at the DataSet layer
5. convert to a GPU notebook
6. figure out how to run the GPU notebook on Google Colab for performance increase
