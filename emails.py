#! /usr/bin/env python3

import os
import mimetypes
import smtplib
from email.message import EmailMessage


def generate_email(has_attachment=False, body="missing", subject="Subject line"):
    attachment_path = "/tmp/processed.pdf"

    message = EmailMessage()
    sender = "automation@example.com"
    # recipient = "student-01-925a7b604c65@example.com"

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    message.set_content(body)
    if has_attachment:
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        print("mime_type: ", mime_type)
        print("mime_subtype: ", mime_subtype)
        with open(attachment_path, "rb") as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)


def send_email(message):
    mail_server = smtplib.SMTP_SSL("34.188.221.42")
    # print("Mailserver response: ", mail_server)
    # mail_server.set_debuglevel(1)
    # mail_pass = "o9UTI78GkCo5"
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)


if __name__ == "__main__":
    subject = "Upload Completed - Online Fruit Store"
    body = """All fruits are uploaded to our successfully. A detailed list is attached to this email."""
    message = generate_email(has_attachment=True, body=body, subject=subject)
    send_email(message)
