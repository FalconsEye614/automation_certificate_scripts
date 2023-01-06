#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body, attachment=None):
    """Create an email object given the Sender, Recipient, Subject, Message Body, and an Attachment (Optional)"""
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment is not None:
        attach_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment, 'rb') as attach:
            message.add_attachment(attach.read(), maintype=mime_type, subtype=mime_subtype, filename=attach_filename)

    return message


def send_email(message):
    """Send an email object using the localhost as the server"""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
