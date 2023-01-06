#!/usr/bin/env python3
from PIL import Image
import glob
import os

# Setup variables
size = (600, 400)
home = os.path.expanduser("~")
directory = home + "/supplier-data/images"

# Iterate through the .TIF image files
for infile in glob.glob(directory+'/*'):
    # Checks if file is in correct format
    f_name, f_ext = os.path.splitext(infile)
    if f_ext != ".tif":
        continue

    # Change .TIF name to JPEG
    strp_file = f_name.split("/")
    outfile = strp_file[-1] + ".jpeg"

    # Resize and convert image files to RGB and JPEG
    try:
        with Image.open(infile) as im:
            out_im = im.resize(size)
            out_im.convert('RGB').save(directory + "/" + outfile, "JPEG")
    except OSError:
        print("cannot convert", infile)
