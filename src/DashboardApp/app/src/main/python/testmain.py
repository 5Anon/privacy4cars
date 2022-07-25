from listfiles import *
import pandas as pd
from upload import *

if __name__ == '__main__':
    files = scanforfiles("..\..\\testdata\\torque")
    for file in files:
        print(f"File Path:{file}")

    mydf = pd.read_csv('..\..\\testdata\\torque\\trackLog-2022-Jun-12_20-42-17.csv')
    mydf.reset_index(drop=True, inplace=True)
    print(mydf)

    upload = Upload("http://localhost:80/api/upload")
    try:
        upload_status = upload.dataframe(mydf)
        if upload_status == 200:
            print("Dataframe has been successfully uploaded")
        else:
            print("Dataframe failed to upload %d" %upload_status)
    except Exception as ex:
        print("Dataframe failed to upload!!!")
        print('[Exception] %s' %ex)

    # runServer()
