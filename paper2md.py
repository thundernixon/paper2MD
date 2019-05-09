import sys
import os
import errno
import re
import certifi
import urllib.request as req

path = sys.argv[1]
workingDir = os.path.split(path)[0]
basename = os.path.split(path)[1]

paperDoc = open(path, "r")

contents = paperDoc.readlines()

# make README file if none exists, otherwise make suffixed file
if os.path.isfile(f"{workingDir}/README.md") != True:
    goodDoc = open(f"{workingDir}/README.md", "w")
else:
    suffixed = basename.replace(".md", "-local.md")
    goodDoc = open(f"{workingDir}/{suffixed}", "w")

# make assets directory
try:
    os.mkdir(f"{workingDir}/assets")
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass


def downloadImage(url, file):
    # open image URL and save to local file
    with req.urlopen(imgUrl, cafile=certifi.where()) as d, open(file, "wb") as opfile:
        data = d.read()
        opfile.write(data)

    print(f"Downloaded \n\t{imgUrl}\nas\n\t{file}")
    print("---------------")


counter = 1

# for line in markdown
for line in contents:
    # if line follows regex of markdown image, download it and write line with local filepath
    regexPattern = re.compile(r'(?:!\[(.*?)\]\((.*?)\))')
    match = regexPattern.findall(line)
    if match != [] and match[0][1] != '/static/img/pixel.gif':
        # download the image into $dir/assets
        imgUrl = match[0][1]
        filetype = imgUrl.split('.')[-1]
        filename = f"fig-{counter}.{filetype}"
        filepath = f"{workingDir}/assets/{filename}"

        downloadImage(imgUrl, filepath)
        counter = counter + 1

        # update markdown file text with local image path

        goodDoc.write(f"![](assets/{filename})\n\n")

        if match[0][0] != '':
            goodDoc.write(f"*{match[0][0]}*\n\n")

    # if line isn't an image, just write it as-is
    else:
        goodDoc.write(line)

# close the good document to save it
goodDoc.close()
