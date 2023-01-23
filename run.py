#! /usr/bin/env python3

import os
import requests


from collections import defaultdict
import json
cwd = os.getcwd()
path = cwd + "/supplier-data/descriptions"
print(path)

txt_file_list = os.listdir(path)
print(txt_file_list)

feedback_from_txt = []
feedback_dictionary = defaultdict(dict)
single_feedback = defaultdict()

fieldnames = ["name", "weight", "description", "image_name"]
ip_address = "35.188.221.42"
url = f"http://{ip_address}/fruits/"
headers = {"content-type": "application/json"}


def upload_descriptions():
    for file in txt_file_list:
        # print("Opening file: {}".format(file))
        with open(path + "/" + file, "r") as feedback:
            single_feedback = defaultdict()
            for index, line in enumerate(feedback):
                if index == 1:
                    single_feedback[fieldnames[index]] = int(line.split(" ")[0])
                    continue
                single_feedback[fieldnames[index]] = line.strip()
            single_feedback[fieldnames[3]] = file.split(".")[0] + ".jpeg"
            feedback_dictionary[file] = single_feedback

# print(feedback_dictionary)

    for file in txt_file_list:
        data = feedback_dictionary[file]
        json_object = json.dumps(data)
        response = requests.post(url, data=json_object, headers=headers)


if __name__ == "__main__":
    upload_descriptions()
