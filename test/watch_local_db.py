#!/usr/bin/python

import boto3
import json
import os
from time import sleep


if __name__ == "__main__":
    db = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

    while True:
        sleep(1)

        table = db.scan(TableName = "my_cookbook_users")

        for item in table['Items']:
            userId = item['userId']['S']
            mapAttr = item['mapAttr']['M']
            os.system("clear");
            print "%s |\t%s" % (userId, json.dumps(mapAttr))
