import requests
from io import StringIO
import pandas as pd

class Upload():
    def __init__(self, serverUrl):
        self.serverUrl = serverUrl

    def daatframeAsBuffer(self, csv_buffer):
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
        status = self.daatframeAsBuffer(csv_buffer)
        return status
