import networkx as nx
import matplotlib.pyplot as plt

# DiGraphs hold directed edges. Self loops are allowed but multiple (parallel) edges are not.
g = nx.read_edgelist("/home/agustin/redRegulatoria_H37RV/mycoRT/DB/2_redT_conOperones_net_number.csv",delimiter=",", nodetype=int, create_using=nx.DiGraph())
print(g.edges())

numero_nodos=nx.number_of_nodes(g)
print(numero_nodos)
numero_ejes=nx.number_of_edges(g)
print(numero_ejes)

betweenness_centrality=nx.betweenness_centrality(g)
print(betweenness_centrality)

distribucion_grados=nx.degree_histogram(g)
print(distribucion_grados)

# nx.draw(g)
# plt.show()

# import powerlaw
# fit = powerlaw.Fit(data)
# fit.power_law.alpha
# fit.power_law.sigma






