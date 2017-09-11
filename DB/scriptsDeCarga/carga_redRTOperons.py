# Cargo la tabla redRTOperons, con mfinderIDs
def carga_redRTOperons():
	# Leo el archivo con la red de Operones pero con mfinderID
	redRT_mfinderID_file=pd.read_csv('2_redT_conOperones_net_number.txt',sep='\s+',header=None)

	# Inicio el cursor
	cursor = cnx.cursor()

	try:
	    for line in range(len(redRT_mfinderID_file)):
	        regulador=int(redRT_mfinderID_file.iloc[line][0])
	        regulado=int(redRT_mfinderID_file.iloc[line][1])
	        add = ("INSERT INTO redRTOperons (A, B) VALUES (%(a)s, %(b)s)")
	        data = {"a": regulador, "b": regulado}
	        cursor.execute(add,data)       
	        cnx.commit()
	finally:  
	    cursor.close()
	return(0)