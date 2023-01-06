# automation_certificate_scripts
These are some of the scripts created to complete the Google IT Automation with Python Courses

__cars.py__
This script imports a json file of a month's car sales report. 
It then unpacks the information and reorganizes it to list to identify:
  - The car that had the most revenue
  - The car that had the most sales
  - The car year with the most sales and how many sales it was
The script then created a PDF with the information below and added a table of all the cars sold sorted by most to least. It then sent an email with the PDF attached to it.

__dailyscripts.py__
This was a fairly simple exercise to run a daily backup script.  The main take away from this script is that it uses multiple cores of the CPU to help lower the amount of time it takes to backup all the files.

__image_cor.py__
This script iterates through a folder full of TIFF images of a wrong size and orientation.  The exercise was to spin all images, resize them to 128x128, and convert them to JPEG image files.

__ticky_check.py__
This exercise asked to use regular expressions to scan through a CRON log list out certain logs to be organized in 2 CSV files:
  - One CSV file listed out the number of each type of ERROR that occured
  - The other CSV file listed out the number of INFO and ERROR entries each user generated

__upload_to_server.py__
This script reads through feedback files, generates a list of dictionaries, then sends each dictionary to the feedback website host as JSON files.

__Final_Lab__
This lab was the final test to obtain the Automation Certificate and is comprised of 7 python scripts. 
The supplier sent the latest fruit images and descriptions to populate the website. The images needed to be reformated both them and the descriptions needed to be loaded onto the website that was created through Django. Once that was finished a PDF report listing all fruits added with their weight needed to be sent back to the supplier via email.
An example of a fruit description is also included. I used it to test out one of the scripts.

  __changeImage.py__
  This script was used to resize the images to 600x400 and reformat them to JPEG since they were sent as TIFF
  
  __supplier_image_upload.py__
  This script uploaded each JPEG images to the website
  
  __run.py__
  This script iterated through each fruit description txt file and generated a list of dictionaries. These dictionaries were used to post the fruits' descriptions to the website through the excepted json format
  
  __report.py__
  This merely created the function to generate the PDF report given the proper format parameters
  
  __email.py__
  Much like report.py, this creates the functions to generate an email object and send the email through the localhost server
  
  __report_email.py__
  This script imports the report.py and email.py functions to organize the information and send and email with the PDF report attached to it
  
  __health_check.py__
  Finally this script was created to check the CPU usage, disk memory usage, RAM availability, and whether the localhost server can be accessed through 127.0.0.1.
  The lab then had us create a CRON job to run this script every minute.
