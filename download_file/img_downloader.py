#!/usr/bin/python3

import sys
import os
import requests

"""
Usage: ./img_downloader <image_url>
"""

image_url = sys.argv[1]
image_r = requests.get(image_url)
header = image_r.headers
img_name = header['X-Clv-Request-Id']
img_name += '.png'
if header['content-type'] == 'image/png' or header['content-type'] == 'image/jpg' or header['content-type'] == 'image/jpeg':
    path = os.path.join(os.getcwd(), img_name)

with open(path, 'wb') as f:
    f.write(image_r.content)

