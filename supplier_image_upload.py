#!/usr/bin/env python3
import requests
import glob
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

for img in glob.glob('/home/student-02-2aa6d7b235d1/supplier-data/images/*.jpeg'):
    with open(img, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
