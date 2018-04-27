#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import powerlaw
import collections
import math

# Leo el archivo de entrada
entrada = pd.read_csv("/home/agustin/redRegulatoria_H37RV/mycoRT/DB/2_redT_conOperones_net_number.csv",header=None)
# Lo transformo en una lista de tuplas
entrada_tuplas = [tuple(x) for x in entrada.values]

# Creo el objeto grafo. No direccionado
ug = nx.Graph()
# Incorporo los nodos
ug.add_edges_from(entrada_tuplas)

# Me quedo con largest connected component
Gc = max(nx.connected_component_subgraphs(ug), key=len)

# Creo el objeto del grafo direccionado
g = nx.DiGraph()
# Le cargo los nodos de la componente principal
g.add_edges_from(Gc.edges())

#¿Cuantos nodos perdi al quedarme solo con la componente principal?
numero_nodos_ug=nx.number_of_nodes(ug)
print(numero_nodos_ug)
numero_nodos_g=nx.number_of_nodes(g)
print(numero_nodos_g)

numero_ejes=nx.number_of_edges(g)
# Centralidad
betweenness_centrality=nx.betweenness_centrality(g)

def grados(distribucion):
    degree_list = []
    for x in distribucion:
        if x[1]!=0:
            degree_list.append(x[1])
    return degree_list

grados_in_degree=grados(g.in_degree)
grados_out_degree=grados(g.out_degree)


def distribucion_grados(lista_grados):
	counter=collections.Counter(lista_grados)
	grado=[]
	cantidad=[]
	for i in counter:
		grado.append(i)
		cantidad.append(counter[i])
	return (grado,cantidad)


# Salida para web
def distribucion_grados_web(lista_grados):
	lista=[]
	counter=collections.Counter(lista_grados)
	for i in counter:
		dict_aux={"x":"","y":""}
		dict_aux["x"]=math.log10(i)
		dict_aux["y"]=math.log10(counter[i])
		lista.append(dict_aux)
	return (lista)

distribucion_grados_in_degree_web=distribucion_grados_web(grados_in_degree)
print(distribucion_grados_in_degree_web)

#~ x=distribucion_grados_in_degree[0]
#~ y=distribucion_grados_in_degree[1]
#~ plt.plot(x,y)
#~ #plt.show()

# Analisis de correlacion power-law
# Lo realizamos con el set de grados_in_degree
fit = powerlaw.Fit(grados_in_degree)

print(fit.power_law.alpha)
print(fit.power_law.sigma)

# Bineado lineal vs Logaritmico
# Por defecto el bineado es logaritmico
fit = powerlaw.Fit(grados_in_degree,discrete=True)
figPDF = powerlaw.plot_pdf(grados_in_degree, color='b')
powerlaw.plot_pdf(grados_in_degree,linear_bins=True, color='r', ax=figPDF)

figPDF.set_ylabel("p(X)")
figPDF.set_xlabel("In degree")
figname = 'FigPDF'
plt.show()
#plt.savefig(figname+'.eps', bbox_inches='tight')
#savefig(figname+'.tiff', bbox_inches='tight', dpi=300)

# Ajuste PowerLaw
fit = powerlaw.Fit(grados_in_degree,discrete=True)
####
figCCDF = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='b', linestyle='--', ax=figCCDF)
####
figCCDF.set_ylabel("p(X)")
figCCDF.set_xlabel("In degree")
figname = 'FigCCDF'
plt.show()
#plt.savefig(figname+'.eps', bbox_inches='tight')
#savefig(figname+'.tiff', bbox_inches='tight', dpi=300)
