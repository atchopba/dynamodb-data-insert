#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Albin TCHOPBA"
# __copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
# __credits__ = ["Albin TCHOPBA and contributors"]
# __license__ = "GPL"
# __version__ = "3"
# __maintainer__ = "Albin TCHOPBA"
# __email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
# __status__ = "Production"

import json
import os
import boto3
import re
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

DYNAMO_HOST = environ.get("DYNAMO_HOST")
DYNAMO_PORT = environ.get("DYNAMO_PORT")

endpoint_url = DYNAMO_HOST if DYNAMO_HOST is not None else None
endpoint_url = endpoint_url + ':' + DYNAMO_PORT if endpoint_url is not None and DYNAMO_PORT is not None else None

ddb = boto3.resource('dynamodb', endpoint_url='http://' + endpoint_url)

arr = os.listdir('./data')

for f in arr:
    # print filename
    print("======> ", f)
    #
    f = open('./data/' + f, "r", encoding="utf-8")
    #
    data = json.load(f)
    # 
    for key_, values_ in data.items():
        # 
        table_ = ddb.Table(key_)
        #
        for putRequest_ in values_:
            # 
            request_ = re.sub(r"'N': '([0-9]+)'", r"'N': \1", str(putRequest_["PutRequest"]["Item"]))
            request_ = re.sub(r"'BOOL': (true|True)", r"'BOOL': 1", str(request_))
            request_ = re.sub(r"'BOOL': (false|False)", r"'BOOL': 0", str(request_)) 
            #
            json_ = json.loads(request_.replace("\'", "\""))
            #
            putRequest_json = {}
            # 
            for k_ in json_:
                #
                for kk in json_[k_]:
                    #
                    putRequest_json[k_] = json_[k_][kk]
            print(putRequest_json)
            table_.put_item(Item=putRequest_json)
