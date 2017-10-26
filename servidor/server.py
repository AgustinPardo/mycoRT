from bottle import get, run, template
from bottle import static_file
from locus_del_operon import *

from gevent import monkey; monkey.patch_all()

@get('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get('/red')
def red():
    with open('Cytoscape-coordenadas/coordenadasConloops.cyjs', 'r') as f:
        read_data = f.read()
        f.close()
    return read_data

@get('/operon/<operon>')
def LDO(operon):    
    salida=locus_del_operon(operon)
    print( salida)
    return {"operones":salida} # Lo tira crudo. Cuando ande terminar.

@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, 
    	root='../web/')




run(host='localhost', port=8080, server='gevent')
