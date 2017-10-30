from __future__ import print_function
import mysql.connector

def data_del_operon(nombre_operon):

	cnx = mysql.connector.connect(user='root', password="agustin", database='mycoDB')

	query_locus= ("SELECT l.locusID FROM operons o, locus l WHERE l.operonID = o.operonID AND l.operonID={};")
	query_regula= ("SELECT o2.operonID FROM operons o, redRTOperons rt, operons o2 WHERE o.mfinderID = rt.A AND o.operonID={} AND o2.mfinderID=rt.B;")
	query_reguladoPor=("SELECT o2.operonID FROM operons o, redRTOperons rt, operons o2 WHERE o.mfinderID = rt.B AND o.operonID={} AND o2.mfinderID=rt.A;")
	query_motivos=("SELECT o2.operonID, o3.operonID, o4.operonID, m.motifType , m.motifID FROM operons o, motifs m, operons o2, operons o3, operons o4 WHERE (o.mfinderID = m.C OR o.mfinderID = m.D OR o.mfinderID = m.E) AND o.operonID={} AND o2.mfinderID=m.C AND o3.mfinderID=m.D AND o4.mfinderID=m.E;") 
	
	data_operon={}

	def cargaIndice(query,name):
		cursor = cnx.cursor()
		cursor.execute(query.format(nombre_operon))
		rows = cursor.fetchall()
		data_operon[name]=rows
		cursor.close()
	
	cargaIndice(query_locus,"locus")
	cargaIndice(query_reguladoPor,"reguladoPor")
	cargaIndice(query_regula,"regula")
	cargaIndice(query_motivos,"motivos")

	cnx.close()

	return (data_operon)
