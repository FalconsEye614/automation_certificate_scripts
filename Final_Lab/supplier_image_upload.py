#!/usr/bin/env python3
import requests
import os
import glob

# Setup directories
url = "http://localhost/upload/"
home = os.path.expanduser("~")
directory = home + "/supplier-data/images"

# Loop through folder to upload JPEG images
for infile in glob.glob(directory+'/*'):
    # Checks if file is a JPEG image
    f_name, f_ext = os.path.splitext(infile)
    if f_ext != ".jpeg":
        continue

    # Post image to local website
    with open(infile, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
