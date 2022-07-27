import cherrypy
import pv
import os
import uploadAPI as du

"""
Default configuration for micro service host
"""
server_conf = {
 'server.socket_host':'0.0.0.0', 
 'server.socket_port': 80,
}

"""
Following path is used for static folder definition to serve static files from webservice
"""
PATH = os.path.abspath(os.path.dirname(__file__))

"""
Setting up log access and error files 
"""
cherrypy.config.update({
    'log.access_file': "privacy4cars_access.log",
    'log.error_file': "privacy4cars_error.log",
    })

"""
MicroService class
"""
class Root(object):
    conf = {
        '/': {
            # serve files on current directory.
            'tools.staticdir.on': True,
            'tools.staticdir.dir': PATH,
            'tools.staticdir.debug': True
        }
    }
    
    @cherrypy.expose
    def index(self):
        return "Privacy for Connected Vehicles!!!"

"""
Method that initializes microservice with appropriate APIs and then starts the service 
"""
def runServer():
    # bind to all IPv4 interfaces
    cherrypy.config.update(server_conf)
    cherrypy.tree.mount(Root(), '/', Root.conf)
    cherrypy.tree.mount(pv.ParameterizationVector(), '/api/pv', pv.ParameterizationVector.conf)
    cherrypy.tree.mount(du.DataUpload(), '/api/upload', du.DataUpload.conf)
    cherrypy.engine.start()
    cherrypy.engine.block()