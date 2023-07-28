import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
input_data = pd.read_csv('D:/VIT/SEM5/B) sin/j comp/adj.csv', index_col=0)
print(input_data)
#print(len(input_data))
G = nx.Graph(input_data.values,with_labels=True)
lbls=[]
for i in range(198):
    lbls.append(i)
labelmap=dict(zip(G.nodes(),lbls))    
print("Degree")
print(G.degree())
print("Normalized Degree Centrality")
print(nx.degree_centrality(G))
print("Closeness Centrality:-")
print(nx.closeness_centrality(G))
print("Betweenness Centrality:-")
print(nx.betweenness_centrality(G,normalized=True,endpoints=False))
nx.draw(G,labels=labelmap,with_labels=True)
plt.show()
