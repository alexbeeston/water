from PIL import Image
import sys, math, os
from pathlib import Path


def process_image(imurl, output):
    im = Image.open(imurl).convert("RGB")
    p = Path(imurl)
    width, height = im.size
    if height > width:
        print("Portrait Image")
        if width > 1440:
            ratio = 1440 / width
            newHeight = math.floor(height * ratio)
            im = im.resize((1440, newHeight))
            height = newHeight
            width = 1440
            print("Resized to " + str(height) + "," + str(width))
        im1 = im.crop((0, 0, width, 1440))
        im2 = im.crop((0, height - 1440, width, height))
        im1.save(output + p.stem + "_1.jpg")
        im2.save(output + p.stem + "_2.jpg")

    elif height < width:
        print("Landscape Image")
        if height > 1440:
            ratio = 1440 / height
            newWidth = math.floor(width * ratio)
            im = im.resize((newWidth, 1440))
            width = newWidth
            height = 1440
            print("Resized to " + str(height) + "," + str(width))
        im1 = im.crop((0, 0, 1440, height))
        im2 = im.crop((width - 1440, 0, width, height))
        im1.save(output + p.stem + "_1.jpg")
        im2.save(output + p.stem + "_2.jpg")
    else:
        print("Square Image")
        if height != 1440:
            im = im.resize((1440, 1440))
        im.save(output + p.stem + ".jpg")


if __name__ == "__main__":
    print("Input directory: " + sys.argv[1])
    print("Output directory: " + sys.argv[2])

    for entry in os.scandir(sys.argv[1]):
        process_image(entry.path, sys.argv[2] + "\\")
