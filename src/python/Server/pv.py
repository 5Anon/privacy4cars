import cherrypy

class ParameterizationVector(object):
    exposed=True
    
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }
    
    # api caller must accept response in json
    def GET(self):
        return "{'Driving Behavior': {'GPS Speed (Meters/second)': [(10,lambda x: ((x >= 0) & (x < 10))), (20,lambda x: ((x >= 10) & (x < 20))), (30,lambda x: ((x >= 20) & (x < 30))), (50,lambda x: ((x >= 30) & (x < 50)))]}, 'Location Data': {' Longitude':[(-121.8,lambda x: (x < -121.8)),(-121.9,lambda x: (x >= -121.8))], ' Latitude':[(38.3,lambda x: (x < 38.3)),(38.4,lambda x: (x >= 38.3))]}}"



        