# Cargo la tabla redRTLocus

def carga_redRTLocus():
    # Leo el archivo con la red de Locus
    redRT_file=pd.read_csv('1_myco_h37rv_RT_locus.txt',sep='\t',header=None)

    # Inicio el cursor
    cursor = cnx.cursor()

    try:
        for line in range(len(redRT_file)):
            nodos=redRT_file.iloc[line][1].split()
            regulador=nodos[0]
            regulado=nodos[1]        
            add = ("INSERT INTO redRTLocus (regulador, regulado) VALUES (%(a)s, %(b)s)")
            data = {"a": regulador, "b": regulado}
            #print(data)
            cursor.execute(add,data)       
            cnx.commit()
    finally:  
        cursor.close()
    return(0)
