#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails



def generate_reportbody(direct):
    """Generate the proper paragraph format for the fruits
       to generate the PDF report given directory of files"""
    # List the files
    fl_lst = os.listdir(direct)
    lst_desc = ""

    for file in fl_lst:
        file_dir = os.path.join(directory, file)
        # Go through each file in the given folder and concatenate
        # each name and weight of fruits loaded on the website
        with open(file_dir, 'rb') as desc:
            txt = []
            for line in desc:
                txt.append(str(line.rstrip(), 'UTF-8'))
            lst_desc = lst_desc + "<br/><br/>name: " + txt[0]
            lst_desc = lst_desc + "<br/>weight: " + txt[1]

    return lst_desc


if __name__ == "__main__":
    # Setup directory for fruit description folder
    home = os.path.expanduser("~")
    directory = os.path.join(home, "supplier-data/descriptions")

    # Generate the PDF for the fruit report
    report_name = "/tmp/processed.pdf"
    report_title = "Processed Update on {}".format(date.today())
    report_desc = generate_reportbody(directory)
    reports.generate_report(report_name, report_title, report_desc)

    # Generate the values for the email to send the report of the uploaded fruits and their weight
    sender = 'automation@example.com'
    recipient = '<username>@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    # Generate an email to send through the localhost
    email = emails.generate_email(sender, recipient, subject, body, report_name)
    emails.send_email(email)
