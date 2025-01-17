import os
import sys
import json
import pymongo

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URl=os.getenv("MONGO_DB_URl")
print(MONGO_DB_URl)

import certifi
ca=certifi.where() 

import numpy as np
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URl)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="lokesh"
    Collection="abc"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(FILE_PATH)
    print(records)
    no_of_record=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_record)