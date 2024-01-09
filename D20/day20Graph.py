import networkx as nx
import matplotlib.pyplot as plt

a = list(open("input"))
parts = {"button": ["b", ["roadcaster"]]}

for line in a:
    b = line.split()
    parts[b[0][1:]] = [b[0][0], [x.strip(",") for x in b[2:]]]

connections = []
for i in parts:
    for j in parts[i][1]:
        connections.append([i,j])

val_map = {"rx":200}
for i in parts:
    if parts[i][0] == "b":
        val_map[i] = 255
    elif parts[i][0] == "%":
        val_map[i] = 0
    elif parts[i][0] == "&":
        val_map[i] = 128
    else:
        val_map[i] = 200

G = nx.DiGraph(directed=True)
G.add_edges_from(connections)

values = [val_map.get(node, 0.25) for node in G.nodes()]

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('hsv'),
                       node_color = values, node_size = 200)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
plt.show()
pass