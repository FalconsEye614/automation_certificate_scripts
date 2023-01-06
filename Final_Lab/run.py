#!/usr/bin/env python3
import os
import requests

# Setup directories to process and upload the fruit descriptions
url = "http://[linux-instance-external-IP]/fruits/"
home = os.path.expanduser("~")
directory = home + "/supplier-data/descriptions"
fl_lst = os.listdir(directory)
lst_desc = []

# Loop through the files to process the fruit descriptions
for file in fl_lst:
    file_dir = os.path.join(directory, file)
    with open(file_dir, 'rb') as desc:
        # Populate list with the fruit descriptions organized into
        # dictionaries for JSON conversion
        txt = []
        fruit_desc = {}
        for line in desc:
            txt.append(str(line.rstrip(), 'UTF-8'))
        fruit_desc["name"] = txt[0]
        weight = int(txt[1].split()[0])
        fruit_desc["weight"] = weight
        fruit_desc["description"] = txt[2]
        image_name = file.split(".")[0] + ".jpeg"
        fruit_desc["image_name"] = image_name
        lst_desc.append(fruit_desc)

# Send each fruit description to the local website as a json file
for fruit in lst_desc:
    r = requests.post(url, json=fruit)
