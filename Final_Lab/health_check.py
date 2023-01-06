#!/usr/bin/env python3
import psutil
import requests
import emails

# Check the CPU usage and check if it is over 80%
cpu_usage = psutil.cpu_percent(interval=1)
cpu_overloaded = cpu_usage > 80

# Check memory storage on disk and check if there's less then 20% free memory
disk_usage = psutil.disk_usage('/')
lack_disk = disk_usage.percent > 80

# Check if the RAM is overloaded. Checks if there's 500MB left available
vmemory = psutil.virtual_memory()
vmem_overloaded = vmemory.available < 500*1024*1024

# Check if the localhost cannot be accessed through 127.0.0.1
response_test = requests.get('http://127.0.0.1/')
response_ok = not response_test.ok

# If any of the above checks are True send an email alert of any checks that came back True
if cpu_overloaded is True or lack_disk is True or vmem_overloaded is True or response_ok is True:
    sender = 'automation@example.com'
    recipient = '<username>@example.com'
    body = 'Please check your system and resolve the issue as soon as possible.'
    if cpu_overloaded is True:
        subject_cpu = 'Error - CPU usage is over 80%'
        email_cpu = emails.generate_email(sender, recipient, subject_cpu, body)
        emails.send_email(email_cpu)
    if lack_disk is True:
        subject_disk = 'Error - Available disk space is less than 20%'
        email_disk = emails.generate_email(sender, recipient, subject_disk, body)
        emails.send_email(email_disk)
    if vmem_overloaded is True:
        subject_vmem = 'Error - Available memory is less than 500MB'
        email_vmem = emails.generate_email(sender, recipient, subject_vmem, body)
        emails.send_email(email_vmem)
    if response_ok is True:
        subject_resp = 'Error - localhost cannot be resolved to 127.0.0.1'
        email_resp = emails.generate_email(sender, recipient, subject_resp, body)
        emails.send_email(email_resp)
