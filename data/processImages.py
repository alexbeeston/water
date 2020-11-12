from PIL import Image
import sys, math, os
from pathlib import Path



def process_image(imurl, output):
    im = Image.open(imurl).convert("RGB")
    p = Path(imurl)
    width, height = im.size
    resolution = 256
    if height > width:
        print("Portrait Image")
        if width > resolution:
            ratio = resolution / width
            newHeight = math.floor(height * ratio)
            im = im.resize((resolution, newHeight))
            height = newHeight
            width = resolution
            print("Resized to " + str(height) + "," + str(width))
        im1 = im.crop((0, 0, width, resolution))
        im2 = im.crop((0, height - resolution, width, height))
        im1.save(output + p.stem + "_1.jpg")
        im2.save(output + p.stem + "_2.jpg")

    elif height < width:
        print("Landscape Image")
        if height > resolution:
            ratio = resolution / height
            newWidth = math.floor(width * ratio)
            im = im.resize((newWidth, resolution))
            width = newWidth
            height = resolution
            print("Resized to " + str(height) + "," + str(width))
        im1 = im.crop((0, 0, resolution, height))
        im2 = im.crop((width - resolution, 0, width, height))
        im1.save(output + p.stem + "_1.jpg")
        im2.save(output + p.stem + "_2.jpg")
    else:
        print("Square Image")
        if height != resolution:
            im = im.resize((resolution, resolution))
        im.save(output + p.stem + ".jpg")


if __name__ == "__main__":
    print("Input directory: " + sys.argv[1])
    print("Output directory: " + sys.argv[2])

    for entry in os.scandir(sys.argv[1]):
        process_image(entry.path, sys.argv[2] + "\\")
