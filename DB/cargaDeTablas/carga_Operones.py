# Cargo la tabla Operones

def carga_Operones():   
    # Leo el archivo donde esta en mfinderID de cada operon
    operonID_mfinderID=pd.read_csv("2_redT_conOperones_fullNames.txt",sep='\t',header=None)
    # Creo un indice donce la llave es el operon y el value el mfinderID
    operonID_mfinderID_Index={}
    # Lleno el indice
    for line in range(len(operonID_mfinderID)):
        operonID_mfinderID_Index[operonID_mfinderID.iloc[line][1]]=int(operonID_mfinderID.iloc[line][0])

    # Leo el archivo con todos los operones
    operon_file=pd.read_csv("1_operones_newID.opr",sep='\t')
    operons=(operon_file["OperonID"])

    # Inicio el cursor
    cursor = cnx.cursor()

    try:  
        for line in list(range(len(operons))): 
            # Inserto los operones y busco en eindice de mfinderID si tienen Id de motivos, sino inserto iun NULL
            # Inserto solo las no repetidas
            add = ("INSERT INTO operons (operonID, mfinderID) VALUES (%(a)s, %(b)s)")
            data = {"a":str(operons[line]), "b": operonID_mfinderID_Index.get(str(operons[line]),None)}
            cursor.execute(add,data)
            cnx.commit()
        for key in operonID_mfinderID_Index:
            # Inserto los operones que son denominados como locus, ya que no estan en ningun operon.
            if key.startswith("rv"):
                add = ("INSERT INTO operons (operonID, mfinderID) VALUES (%(a)s, %(b)s)")
                data = {"a":key, "b": operonID_mfinderID_Index[key]}
                cursor.execute(add,data)
                cnx.commit()
                
    finally:  
        cursor.close()

    return(0)    
