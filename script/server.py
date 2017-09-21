from bottle import get, run, template
from bottle import static_file

@get('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

 # Tiro la query a la DB, y cargo los datos
 # Busco la red regulatoria de operones y 
 # creo dos indices con el formato Json (JavaScript Object Notation).

@get('/red')
def red():
    return { "nodos" : [
  {"rv":"Rv0667"},
  {"rv":"Rv0668"}
    ] , "aristas":[{"rv1":"Rv0667","rv2":"Rv0668"}] }

@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, 
    	root='/home/agustin/Red Regulatoria-H37RV/mycoRT/web/')
"""
@get('/')
def inicio():
	return s
""
run(host='localhost', port=8080)