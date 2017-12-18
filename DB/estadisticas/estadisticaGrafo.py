import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import powerlaw


# DiGraphs hold directed edges. Self loops are allowed but multiple (parallel) edges are not.
# g = nx.read_edgelist("/home/agustin/redRegulatoria_H37RV/mycoRT/DB/2_redT_conOperones_net_number.csv",delimiter=",", nodetype=int, create_using=nx.DiGraph())

entrada = pd.read_csv("/home/agustin/redRegulatoria_H37RV/mycoRT/DB/2_redT_conOperones_net_number.csv",header=None)
entrada_tuplas = [tuple(x) for x in entrada.values]

ug = nx.Graph()
ug.add_edges_from(entrada_tuplas)  # undirected global graph; edgetable is just a list of A->B, A->C, C->D etc.

# largest connected component
Gc = max(nx.connected_component_subgraphs(ug), key=len)

g = nx.DiGraph()
g.add_edges_from(Gc.edges())  # directed global graph from the largest connected component



numero_nodos_ug=nx.number_of_nodes(ug)
print(numero_nodos_ug)

numero_nodos_g=nx.number_of_nodes(g)
print(numero_nodos_g)


numero_ejes=nx.number_of_edges(g)
betweenness_centrality=nx.betweenness_centrality(g)

def grados(distribucion):
    degree_list = []
    for x in distribucion:
        if x[1]!=0:
            degree_list.append(x[1])
    return degree_list


data2=grados(g.in_degree)
data=grados(g.out_degree)

plt.plot(sorted(data,reverse=True))
plt.show()


fit = powerlaw.Fit(data)
print(fit.power_law.alpha)
print(fit.power_law.sigma)

####
print(powerlaw.pdf(data))
powerlaw.plot_pdf(data,linewidth=2)

powerlaw.plot_pdf(data, linear_bins=True, color='r')
plt.show()

powerlaw.plot_cdf([data])

#
# figPDF = powerlaw.plot_pdf(data, color='b')
# powerlaw.plot_pdf(data, linear_bins=True, color='r', ax=figPDF)
# fit.power_law.plot_pdf(color='b', linestyle='--', ax=figPDF)
# ####
# figPDF.set_ylabel("p(X)")
# figPDF.set_xlabel(r"In degree")
# figname = 'FigPDF'
# plt.savefig(figname+'.eps', bbox_inches='tight')
# #savefig(figname+'.tiff', bbox_inches='tight', dpi=300)

plt.show()

