import cherrypy
from cherrypy import tools
import pandas as pd
from io import StringIO

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
            cherrypy.log.access_log.info("Request content is saved to dataframe of shape = {}".format(df.shape))
        except Exception as err:
            cherrypy.log.error_log.exception(f"Unexpected {err=}, {type(err)=}")
            print(f"Unexpected {err=}, {type(err)=}")
            return "{'upload':0}"

        cherrypy.response.status = 200
        return "{'upload':1}"