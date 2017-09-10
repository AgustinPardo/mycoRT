# Cargo la tabla motifs
def carga_motifs():
    # Leo el archivo donde estan los motifs
    motifs_file=open("3_mfinderMycoh37rv_MEMBERS.txt","r")

    # Inicio el cursor
    cursor = cnx.cursor()

    try:
        for line in motifs_file:      
            if str(line[0:8]) == "subgraph":
                tipoDeMotivo= int(line.split(" ")[3].rstrip())
            if line[0].isdigit():
                motivos=line.split("\t")
                C=motivos[0]
                D=motivos[1]
                E=motivos[2]       
                add = ("INSERT INTO motifs (C, D, E, motifID) VALUES (%(a)s, %(b)s, %(c)s, %(d)s)")
                data = {"a": C, "b": D, "c": E, "d":tipoDeMotivo}
                #print(data)
                cursor.execute(add,data)       
                cnx.commit()
    finally:  
        cursor.close()
        motifs_file.close()
    return(0)
