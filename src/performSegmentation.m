function outputIm = performSegmentation(inputIm)
outputIm = inputIm;
outputIm = medfilt2(outputIm);
outputIm = edge(outputIm);
outputIm = imclose(outputIm, strel('disk', 4));
outputIm = medfilt2(outputIm);
outputIm = imdilate(outputIm, strel('disk', 2));
end

