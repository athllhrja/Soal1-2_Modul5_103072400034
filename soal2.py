import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

edges = [
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Semarang", "Yogyakarta", 109),
    ("Semarang", "Surakarta", 97),
    ("Yogyakarta", "Surakarta", 60),
    ("Surakarta", "Malang", 370),
    ("Semarang", "Surabaya", 369),
    ("Surabaya", "Malang", 94)
]

G.add_weighted_edges_from(edges)

# BFS
bfs_nodes = list(nx.bfs_tree(G, source="Bandung"))
print("BFS dari Bandung:", bfs_nodes)

# Visualisasi
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))

nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Graf Pulau Jawa")
plt.show()
