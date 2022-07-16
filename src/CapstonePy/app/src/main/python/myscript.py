#Python Script

import numpy as np
import pandas
import csv
import time
import datetime
import mysql.connector

import socket
#import sys

import requests


def main():
	#f = open('/data/data/com.example.capstonepy/shared_prefs/save.xml')
	#print(f.read())
    

    # try:
        
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect(('192.168.0.26', 8888)) #IP is the server IP
     
        
        # msg = "Hi Privacy4Cars !"
         
        # s.send(msg.encode())

     
        # return 'Testing Functionality'
                
    # except Exception as e:
        # return e

	return 'Testing Privacy4Cars Outout'
    
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
    