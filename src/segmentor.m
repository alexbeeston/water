clc;
close all;
clear variables;

testim = rgb2gray(imread("K_32_crack_raw_2.jpg"));
testout = performSegmentation(testim);


figure
subplot(1, 2, 1), imshow(testim);
subplot(1, 2, 2), imshow(mat2gray(bwskel(testout, 'MinBranchLength', 10)));

testblah = bwskel(testout, 'MinBranchLength', 15);
pathImage(testblah);

imwrite(testblah, "testoutput.png");

pause;
close all;
clear variables;