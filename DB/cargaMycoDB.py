from __future__ import print_function
import mysql.connector
import pandas as pd

import sys
import os
# Incorporo el path donde estan los archivos de carga individuales de cada Tabla
sys.path.append(os.getcwd()+"/cargaDeTablas")

from carga_Operones import *
from carga_locus import *
from carga_redRTOperons import *
from carga_redRTLocus import *
from carga_motifs import *

cnx = mysql.connector.connect(user='root', password="agustin", database='mycoDB')

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

# Como ejecutar las funciones en Orden?????###
carga_Operones()
carga_locus()
carga_motifs()
carga_redRTOperones()
carga_redRTLocus()

