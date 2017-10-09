from bottle import get, run, template
from bottle import static_file
from redOperonesJSON import *

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

@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, 
    	root='../web/')

@get('/')
def inicio():
	return s

run(host='localhost', port=8080, server='gevent')