import cherrypy

class ParameterizationVector(object):
    exposed=True
    
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }
    
    # api caller must accept response in json
    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_out()
    def GET(self):
        return {'location':'hsks*lk', 'drivingbehavior':'*'}       