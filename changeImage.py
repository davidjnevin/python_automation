#! /usr/bin/env python3

from PIL import Image, UnidentifiedImageError
import os
from pathlib import Path
import filetype

filenames = []

src = Path.cwd().joinpath(r"supplier-data/images")
dest = Path.cwd() / "supplier-data" / "images"


def change_image():
    try:
        dest.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already there")
    else:
        print("Folder created")
    for root, dirs, files in os.walk(src, topdown=True):
        for file in files:
            filename = root + "/" + file
            if not filetype.is_image(filename):
                continue
            try:
                im = Image.open(filename).convert("RGB")
                im = im.resize((600, 400))
                file_new = file.split(".")[0] + ".jpeg"
                im.save(f"{dest}/{file_new}", format="jpeg")
            except UnidentifiedImageError as e:
                print(f"Unable to process {file}: error {e}")
                continue
            except FileNotFoundError as e:
                print(f"Unable to open  {file}: error {e}")
                continue
            print(f"Saved {file_new} to {dest}")


if __name__ == "__main__":
    change_image()
