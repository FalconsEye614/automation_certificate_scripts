#!/usr/bin/python3
from PIL import Image
import glob
import os

# Set size the pictures need to be
size = (128, 128)

# Iterate through the current folder to find the .tiff images,
# convert them to .jpg, rotate them clockwise 90 degrees,
# and resize them to a size specifed above.
for infile in glob.glob("./images/*"):
    f_name, f_ext = os.path.splitext(infile)
    strp_file = f_name.split("/")
    outfile = strp_file[-1] + ".jpg"
    try:
        with Image.open(infile) as im:
            out_im = im.resize(size).rotate(270)
            out_im.convert('RGB').save("/opt/icons/" + outfile, "JPEG")
    except OSError:
        print("cannot convert", infile)