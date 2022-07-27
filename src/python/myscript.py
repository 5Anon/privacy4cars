#Python Script

from io import StringIO
import numpy as np
import pandas as pd
# import csv
# import time
# import datetime
# import mysql.connector
# import shutil
# import os
# import stat
# import subprocess
# import math
# from dateutil import parser
import socket
import requests


def main():
    try:
        xml_file_path = "/data/data/com.example.capstonepy/shared_prefs/save.xml"
        [maintenance_privacy_setting,driving_privacy_setting,location_privacy_setting,vision_privacy_setting] = getSaveXMLData(xml_file_path)
        parameters = getParameterizationVectors() # TO-DO: NEED TO UPDATE THE API WITH CAR DATA VALUES AFTER ANONYMIZATION METRICS
        dest = r'/data/data/com.example.capstonepy/files/trackLog-2022-Jun-17_11-17-49.csv'
        data =  preprocessData(dest,'car70')
        meta_data = []
        if(driving_privacy_setting):
            data = Anonymizer(parameters["Driving Behavior"], data) # TO-DO: NEED TO ADD CAR DATA TO ENABLE MORE QUASI-IDENTIFIERS
            meta_data.extend(parameters["Driving Behavior"].keys())
        if(location_privacy_setting):
            data = Anonymizer(parameters["Location Data"], data) # TO-DO: NEED TO ADD CAR DATA TO ENABLE MORE QUASI-IDENTIFIERS
            meta_data.extend(parameters["Location Data"].keys())
        Meta_Data_col = [str(meta_data)]*len(data)
        data.insert(loc=1, column="Meta_Data",value=Meta_Data_col)
        uploadData = Upload('http://privacyforconnectedvehiclesapi.westus3.cloudapp.azure.com:3999/api/upload')
        uploadData.dataframe(data)
        return "Data Uploaded!"
    except Exception as e:
        return "Data Upload Failed: "

def getSaveXMLData(path):
    xml_file = open("/data/data/com.example.capstonepy/shared_prefs/save.xml")
    xml_file = xml_file.readlines()
    maintenace = False
    driving = False
    location = False
    vision =  False
    if 'true' in xml_file[2]:
        maintenace = True
    if 'true' in xml_file[3]:
        driving = True
    if 'true' in xml_file[4]:
        location = True
    if 'true' in xml_file[5]:
        vision = True
    return [maintenace, driving, location, vision]

def getParameterizationVectors():
  r = requests.get("http://privacyforconnectedvehiclesapi.westus3.cloudapp.azure.com:3999")
  if(r.status_code == 200):
    print(r.text)
    r = requests.get("http://privacyforconnectedvehiclesapi.westus3.cloudapp.azure.com:3999/api/pv")
    if(r.status_code == 200):
      try:
        param = eval(r.text)
        return param
      except:
        return None
  return None

def Anonymizer(parameters, data): # TO-DO: Iterate through the Main Dictionary and Call the Anonymizer Function for Each
  d = data.copy()
  for key,value in parameters.items():
    for val,val_func in value:
        d = d[d[key].notna()]
        d.loc[val_func(d[key]),key] = val
  return d

def preprocessData(path,carID):
    accepted_types = set({pd._libs.tslibs.timestamps.Timestamp,str, pd._libs.tslibs.nattype.NaTType, float})
    # Reading the data
    raw_data = pd.DataFrame()
    data_temp = pd.read_csv(path)
    raw_data = raw_data.append(data_temp, ignore_index=True, sort=False)
    raw_data = raw_data.drop(raw_data[raw_data["GPS Time"] == "GPS Time"].index)
    raw_data = pd.DataFrame(np.where( raw_data == "-", 0, raw_data), columns=raw_data.columns)
    # raw_data["Cost per mile/km (Instant)($/m)"] = 0
    # raw_data = raw_data[raw_data[' Horizontal Dilution of Precision'].notna()]
    for col in raw_data.columns[2:]:
        raw_data[col] = raw_data[col].astype(float, errors='ignore')
    carID_col = [carID]*len(raw_data)
    raw_data.insert(loc=0, column="carID",value=carID_col)

    return raw_data

class Upload():
    def __init__(self, serverUrl):
        self.serverUrl = serverUrl

    def dataframeAsBuffer(self, csv_buffer):
        """
        Uploads a dataframe as string buffer
        :param csv_buffer: dataframe buffer as string
        :return: status code - 200 - Success, anything else is error
        """
        print(csv_buffer.getvalue())
        r = requests.post(self.serverUrl, data=csv_buffer.getvalue().encode('utf-8'))
        return r.status_code

    def dataframe(self, df):
        """
        Uploads a dataframe object
        :param df: Dataframe object
        """
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        df.reset_index(drop=True, inplace=True)
        status = self.dataframeAsBuffer(csv_buffer)
        return status


def locationFunction():

    while True:
    
        try:
                  
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.0.26', 8888)) #IP is the server IP
            msg = "Testing Location Switch"
             
            s.send(msg.encode())
         
            return 'Testing switch!'
                    
        except Exception as e:
            return e
        


def visionFunction():


    try:
              
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.26', 8888)) #IP is the server IP
        msg = "Testing Vision Switch"
         
        s.send(msg.encode())
     
        return 'Testing switch!'
                
    except Exception as e:
        return e


def maintenanceFunction():


    try:
              
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.26', 8888)) #IP is the server IP
        msg = "Testing Maintenance Switch"
         
        s.send(msg.encode())
     
        return 'Testing switch!'
                
    except Exception as e:
        return e


def drivingFunction():


    try:
              
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.26', 8888)) #IP is the server IP
        msg = "Testing Driving Behavior Switch"
         
        s.send(msg.encode())
     
        return 'Testing switch!'
                
    except Exception as e:
        return e


def bluetoothFunction():


    try:
              
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.26', 8888)) #IP is the server IP
        msg = "Testing Bluetooth Switch"
         
        s.send(msg.encode())
     
        return 'Testing switch!'
                
    except Exception as e:
        return e
    