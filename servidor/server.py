from bottle import get, run, template
from bottle import static_file
from data_del_operon import *

from gevent import monkey; monkey.patch_all()

@get('/red')
def red():
    with open('Cytoscape-coordenadas/coordenadasConloops.cyjs', 'r') as f:
        read_data = f.read()
        f.close()
    return read_data

@get('/operon/<operon>')
def LDO(operon):
    salida=data_del_operon(operon) 
    return salida

@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, 
    	root='../web/')

run(host='localhost', port=8080, server='gevent')

