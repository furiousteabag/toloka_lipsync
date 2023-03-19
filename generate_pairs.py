SOURCE_FOLDER = "lipsyncer"
SOURCE_LANG = "eng"

import os

folders = [f for f in os.listdir() if os.path.isdir(f) and f != ".git"]
folders.remove(SOURCE_FOLDER)

print(folders)

pairs = []

prefix = "https://github.com/SmirnovAlexander/toloka_lipsync/blob/main/"
suffix = "?raw=true"

for folder in folders:
    for filename in os.listdir(os.path.join(SOURCE_FOLDER, SOURCE_LANG)):
        pair = [prefix + os.path.join(SOURCE_FOLDER, SOURCE_LANG, filename) + suffix, prefix + os.path.join(folder, SOURCE_LANG, filename) + suffix]
        pairs.append(pair)

print(pairs)
