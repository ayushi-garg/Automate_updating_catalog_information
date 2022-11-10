#! /usr/bin/env python3

import os
import requests
import json
text_files = os.listdir("/home/student-02-a90500197f9a/supplier-data/descriptions/")
# data_dict = {"title":"test","name":"test","date":"test","feedback":"test"} 
data_dict = {} 

for txt in text_files: 
    with open("/home/student-02-a90500197f9a/supplier-data/descriptions/"+txt) as fileobj:
        list_of_entries = fileobj.readlines()
        data_dict["name"] = list_of_entries[0].strip()
        data_dict["weight"] = list_of_entries[1].strip()[:-4]
        data_dict["description"] = list_of_entries[2].strip()
        data_dict["image_name"] = txt[:-3]+"jpeg"
    print(data_dict)   
    # print(type(data_dict)) 
    # data_dict = json.dumps(data_dict,indent=2)
    # # print(list_of_entries)
    # print(data_dict)
    response = requests.post("http://localhost/fruits/",json=data_dict)
    print(response.status_code)
    response.raise_for_status()
