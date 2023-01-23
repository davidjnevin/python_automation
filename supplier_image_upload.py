#! /usr/bin/env python3

import requests
import os
from pathlib import Path

src = Path.cwd().joinpath(r"supplier-data/images")

url = "http://localhost/upload/"


def upload_images(src, url):
    for root, dirs, files in os.walk(src, topdown=True):
        print(root, dirs, files)
        for file in files:
            if ".jpeg" in file:
                filename = root + "/" + file
                with open(filename, 'rb') as opened:
                    r = requests.post(url, files={'file': opened})
                print("Send: ", file)
            else:
                continue


if __name__ == "__main__":
    upload_images(src=src, url=url)
