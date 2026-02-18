import os
import json
import sys


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi

ca=certifi.where()

import pandas as pd
import numpy as np

import pymongo
from networksecurity.exception.exception import NetworkSecurityException    
from networksecurity.logging.logger import logging

class NetworkDataExtract:

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json(self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            print(data.head())
            data.reset_index(drop=True, inplace=True)
            logging.info(f"Data extracted from {file_path} successfully.")
            records =data.to_dict(orient="records")
             # Print first 5 records
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return (len(self.records))
            logging.info(f"Data inserted into {self.collection.name} successfully.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    try:
        logging.info("Testing NetworkDataExtract")
        data_extractor = NetworkDataExtract()
        data = data_extractor.cv_to_json("network_data/phisingData.csv")
        data_extractor.insert_data_mongodb(data, "network_security", "network_security")
       # print(data[:5])
    except Exception as e:
        raise NetworkSecurityException(e, sys)