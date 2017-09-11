# Cargo la tabla locus

def carga_locus():
    # Leo el archivo con todos los locus
    loci_file=open("listaDelocush37rv.txt","r")
    # Leo el archivo con todos los operones
    operones_file=pd.read_csv('1_operones_newID.opr',sep='\t')

    # Parseo operones y creo un indice de operones-locus
    index_loci_operon={}
    operon= operones_file["OperonID"]
    locusID= operones_file["Synonym"]
    for fila in list(range(len(operon))):
        index_loci_operon[locusID[fila]]=int(operon[fila])
         
    # Inicio el cursor
    cursor = cnx.cursor()
    try:
        for locus in loci_file:
            locus=locus.rstrip()
            add = ("INSERT INTO locus (locusID, operonID) VALUES (%(a)s, %(b)s)")
            data = {"a": locus, "b": index_loci_operon.get(str(locus),None)}
            cursor.execute(add,data)       
            cnx.commit()
    finally:  
        cursor.close()
        loci_file.close()
        
    return(0)