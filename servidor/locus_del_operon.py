from __future__ import print_function
import mysql.connector

def locus_del_operon(nombre_operon):

	cnx = mysql.connector.connect(user='root', password="mito", database='mycoDB')
	cursor = cnx.cursor()

	# Query
	query = (
	  "SELECT l.locusID FROM operons o, locus l WHERE l.operonID = o.operonID AND l.operonID={} LIMIT 10;".format(nombre_operon))
	cursor.execute(query)

	# Capturo la Query 
	rows = cursor.fetchall()
	#print(rows)

	cursor.close()
	cnx.close()

	return (rows)

#locus_del_operon("1132838")