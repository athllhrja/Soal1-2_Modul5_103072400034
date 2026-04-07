import networkx as nx
import matplotlib.pyplot as plt

# Membuat graph
G = nx.Graph()

edges = [
    ("Arad", "Zerind", 75), 
    ("Arad", "Sibiu", 140), 
    ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Sibiu", "Fagaras", 99), 
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146), 
    ("Craiova", "Pitesti", 138),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98), 
    ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]

G.add_weighted_edges_from(edges)

# DFS Edge
dfs_edges = list(nx.dfs_edges(G, source="Arad"))
print("DFS edges dari Arad:")
for edge in dfs_edges:
    print(edge)

# Visualisasi
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(11, 9))

# Gambar semua graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500)

# Ambil bobot edge
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight jalur DFS (warna merah)
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='red', width=2)

plt.title("Graf Eropa (DFS Edge dari Arad)")
plt.show()
