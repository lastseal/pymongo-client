#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pymongo import MongoClient

import json

host = "127.0.0.1"
port = 27017
username = "test"
password = "test"

dbname = "test"
collectionName = "test"

try:

    client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}")

    db = client[dbname]
    collection = db[collectionName]

    # Insertando un sólo documento en la colección

    doc = {
        "author": "Lastseal",
        "text": "Ejemplo de documento",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.utcnow()
    }

    collection.insert_one(doc)

    print( collection.find_one() )

    # Insertando múltiples documentos

    docs = [
        {
            "author": "developer 1",
            "text": "Primer documento",
            "tags": ["bulk", "insert"],
            "date": datetime(2021, 12, 1, 11, 14)
        },
        {
            "author": "developer 2",
            "text": "Segundo documento",
            "date": datetime(2021, 12, 2, 10, 45)
        }
    ]

    collection.insert_many(docs)

    for doc in collection.find():
        print(doc)

except Exception as ex:
    print(ex)
