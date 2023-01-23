#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
from collections import defaultdict
import os

def generate_title(title):
    todays_date = date.today()
    return "{title} {todays_date}"

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


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()

    report_name = f"{attachment}"
    data = []
    report = SimpleDocTemplate(report_name)
    report_title = generate_title(title)
    report_title = Paragraph(report_title, styles["h1"])

    data.append(report_title)

    body = paragraph

    report_body = Paragraph(body, styles["BodyText"])

    data.append(report_body)

    report.build(data)


if __name__ == "__main__":
    generate_report("processed.pdf", "Processed Update on ", generate_paragraph())

