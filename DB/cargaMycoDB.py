from __future__ import print_function
import mysql.connector
import pandas as pd

import carga_Operones
import carga_locus
import carga_redRTLocus
import carga_redRTOperones
import carga_motifs

cnx = mysql.connector.connect(user='root', password="agustin", database='mycoDB')
print(cnx)

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

carga_Operones()
carga_locus()
carga_motifs()
carga_redRTOperones()
carga_redRTLocus()

