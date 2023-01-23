#! /usr/bin/env python3

import reports
import os
import mimetypes
import smtplib
from collections import defaultdict
from email.message import EmailMessage


attachment_path = "/tmp/processed.pdf"
title = "Processed Update on "


def generate_paragraph():
    summary = []

    cwd = os.getcwd()
    path = cwd + "/supplier-data/descriptions"

    txt_file_list = os.listdir(path)

    fruit_dictionary = defaultdict(dict)
    single_fruit = defaultdict()

    fieldnames = ["name", "weight", "description", "image_name"]

    for file in txt_file_list:
        with open(path + "/" + file, "r") as fruit:
            single_fruit = defaultdict()
            for index, line in enumerate(fruit):
                if index == 1:
                    single_fruit[fieldnames[index]] = int(line.split(" ")[0])
                    continue
                single_fruit[fieldnames[index]] = line.strip()
            single_fruit[fieldnames[3]] = file.split(".")[0] + ".jpeg"
            fruit_dictionary[file] = single_fruit

    for file in txt_file_list:
        summary.append("<br></br>")
        summary.append("name: {}".format(fruit_dictionary[file]["name"]))
        summary.append("weight: {} lbs".format(fruit_dictionary[file]["weight"]))

    body = "<br></br>".join(summary)
    return body


attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split("/", 1)

message = EmailMessage()
sender = "automation@example.com"
recipient = "student-01-925a7b604c65@example.com"

message["From"] = sender
message["To"] = recipient
message["Subject"] = "Upload Completed - Online Fruit Store"

body = """All fruits are uploaded to our successfully. A detailed list is attached to this email."""

message.set_content(body)

with open(attachment_path, "rb") as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

    print(message)

    mail_server = smtplib.SMTP("34.188.221.42")
    print("Mailserver response: ", mail_server)
    mail_server.set_debuglevel(1)
    mail_pass = "o9UTI78GkCo5"
    mail_server.login(recipient, mail_pass)

    mail_server.send_message(message)


if __name__ == "__main__":
    paragraph = generate_paragraph()
    reports.generate_report(attachment_path, title, paragraph)
