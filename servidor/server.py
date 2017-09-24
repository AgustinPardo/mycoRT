from bottle import get, run, template
from bottle import static_file
from redOperonesJSON import *

@get('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

 # Tiro la query a la DB, y cargo los datos
 # Busco la red regulatoria de operones y 
 # creo dos indices con el formato Json (JavaScript Object Notation).

# Funcion que llama la Query de la red


@get('/red')
def red():
	return redRTOperones()

@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, 
    	root='/home/pardo/Documentos/mycoRT/mycoRT/web/')

@get('/')
def inicio():
	return s

run(host='localhost', port=8080)