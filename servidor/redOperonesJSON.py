from __future__ import print_function
import mysql.connector

def redRTOperones():

	cnx = mysql.connector.connect(user='root', password="agustin", database='mycoDB')
	cursor = cnx.cursor()

	# Query
	query = (
	  "SELECT o1.operonID, o2.operonID FROM operons o1, operons o2, redRTOperons r WHERE o1.mfinderID = r.A AND o2.mfinderID = r.B;")
	cursor.execute(query)

	# Capturo la Query y la pongo en una lista de tuplas.
	rows = cursor.fetchall()

	listaAristas=[]
	listaNodos=[]
	listaControl=[]
	
	
	for row in rows:
		listaAristas.append({"op1":row[0],"op2":row[1]})
		for elem in row:
			if elem not in listaControl:
				listaNodos.append({"rv":elem})
			listaControl.append(row)

	nodosAristas={}
	nodosAristas["nodos"]=listaNodos
	nodosAristas["aristas"]=listaAristas

	cursor.close()
	cnx.close()

	print(nodosAristas)	

	

