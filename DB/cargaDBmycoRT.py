
# coding: utf-8

# In[209]:

# librerias
from __future__ import print_function
import mysql.connector
import pandas as pd
#import glob
#import re


# In[210]:

# Me conecto a la base de datos
cnx = mysql.connector.connect(user='root', password="agustin", database='mycoDB')
print(cnx)


# In[211]:

# Borro los datos de las tablas

try:
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM motifs")
    cursor.execute("DELETE FROM redRTLocus")
    cursor.execute("DELETE FROM redRTOperons")
    cursor.execute("DELETE FROM locus")
    cursor.execute("DELETE FROM operons")
    cnx.commit()
    print(cnx.commit())
    
finally:
    cursor.close()


# In[212]:

# Cargo la tabla Operones

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

print("OK")    


# In[213]:

# Cargo la tabla locus

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
i=0
try:
    for locus in loci_file:
        i=i+1
        locus=locus.rstrip()
        add = ("INSERT INTO locus (locusID, operonID) VALUES (%(a)s, %(b)s)")
        data = {"a": locus, "b": index_loci_operon.get(str(locus),None)}
        #print(data)
        cursor.execute(add,data)       
        cnx.commit()
finally:  
    cursor.close()
    loci_file.close()
    
print("OK")


# In[214]:

# Cargo la tabla redRTLocus

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
print("OK")


# In[215]:

# Cargo la tabla redRTOperons, con mfinderIDs

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
print("OK")


# In[216]:

# Cargo la tabla motifs

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
print("OK")


# In[ ]:




# In[ ]:



