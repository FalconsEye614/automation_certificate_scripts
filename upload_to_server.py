#! /usr/bin/env python3
import os
import requests

# Get list of files
fl_lst = os.listdir("/data/feedback")
lst_feedback = []

# Iterate through files
for file in fl_lst:
    # Add directory to file
    file_dir = "/data/feedback/" + file
    # Open file and add content to list of dictionaries
    with open(file_dir, "r") as fl:
        txt = []
        review = {}
        for line in fl:
            txt.append(line.rstrip())
        review["title"] = txt[0]
        review["name"] = txt[1]
        review["date"] = txt[2]
        review["feedback"] = txt[3]
        lst_feedback.append(review)

# Iterate through list of feedbacks to send each to the web service
for feedback in lst_feedback:
    web_resp = requests.post("http://<corpweb-external-IP>/feedback", json=feedback)
    print(web_resp.status_code)
