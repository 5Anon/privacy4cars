import cherrypy
from cherrypy import tools
import pandas as pd
from io import StringIO
import pyodbc
import numpy as np
import time
import math

cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:privacyforcars.database.windows.net,1433;Database=HistoricalDatabase;Uid=PfCCAdmin;Pwd={PrivacyForConnectedCars101#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

class DataUpload(object):
    exposed=True
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }

    # api caller must accept response in json
    @tools.decode(encoding='utf-8')
    def POST(self):
        try:
            cherrypy.response.status = 500
            # conn = pymssql.connect(server='privacyforcars.database.windows.net',user='PfCCAdmin',password='PrivacyForConnectedCars101#',database='HistoricalDatabase')
            # get the content length information
            cl = cherrypy.request.headers['Content-Length']
            cherrypy.log.access_log.info("Received request with content length = {}".format(int(cl)))
            # read data from request body
            data = cherrypy.request.body.read(int(cl))
            # decode the data as it is utf-8 encoded
            body = data.decode('utf-8')
            # create dataframe object from the body
            csv_buffer = StringIO(body)
            df = pd.read_csv(csv_buffer)
            # ensuring that there is not unnamed index in the dataframe
            df.reset_index(drop=True, inplace=True)
            for ind,row in df.iterrows():
                try:
                    cursor.execute(
                        "INSERT INTO HistoricalDatabase.dbo.OriginalDataset VALUES "+
                        "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?)", tuple(row))
                    cursor.commit()
                    cursor.execute(
                        "INSERT INTO HistoricalDatabase.dbo.AnonMetaData VALUES "+
                        "(?, ?, ?)", tuple(row[0:3]))
                    cursor.commit()
                    cursor.execute(
                        "INSERT INTO HistoricalDatabase.dbo.CarCloudDataBase VALUES "+
                        "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"+
                        " ?, ?, ?, ?, ?)", tuple(row.drop("Meta_Data")))
                    cursor.commit()
                except Exception as e:
                    print(e)
            cherrypy.log.access_log.info("Request content is saved to dataframe of shape = {}".format(df.shape))
        except Exception as err:
            # cherrypy.log.error_log.exception(f"Unexpected {err=}, {type(err)=}")
            # print(f"Unexpected {err=}, {type(err)=}")
            print(err)
            return "{'upload':0}"

        cherrypy.response.status = 200
        return "{'upload':1}"