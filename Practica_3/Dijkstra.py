# Datos personales
# Nombre: Miguel Angel Huerta Castillo
# Registro: 21310236

# Título: Simulador del Algoritmo de Dijkstra con Interfaz Gráfica
# Descripción: Este programa simula el funcionamiento del Algoritmo de Dijkstra para encontrar el camino más corto en un grafo ponderado. Muestra los resultados en una interfaz gráfica utilizando la biblioteca networkx.

import networkx as nx
import matplotlib.pyplot as plt

# Implementación del Algoritmo de Dijkstra
def dijkstra(graph, start_node):
    nodes = list(graph.keys())
    visited = {node: False for node in nodes}
    distances = {node: float('inf') for node in nodes}
    distances[start_node] = 0
    path = {node: None for node in nodes}

    current_node = start_node

    while True:
        visited[current_node] = True
        for neighbor, weight in graph[current_node].items():
            if not visited[neighbor]:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = current_node

        next_node = None
        min_distance = float('inf')
        for node in nodes:
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                next_node = node

        if next_node is None:
            break
        current_node = next_node

    return distances, path

# Definición del grafo de ejemplo
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2},
    'C': {'B': 5, 'D': 5, 'E': 3},
    'D': {'A': 1, 'B': 2, 'C': 5, 'E': 4},
    'E': {'C': 3, 'D': 4}
}

# Ejecución del algoritmo
start_node = 'A'
distances, path = dijkstra(graph, start_node)

# Creación del grafo con networkx
G = nx.Graph()
for node in graph:
    G.add_node(node)
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

# Obtención de posiciones para los nodos
pos = nx.spring_layout(G)

# Dibujo del grafo
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=16, font_weight='bold')

# Dibujo de las aristas con pesos
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=12)

# Resaltado del camino más corto desde el nodo inicial
path_edges = [(path[node], node) for node in path if path[node] is not None]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)

# Mostrar distancia mínima y camino para cada nodo
plt.title("Simulador del Algoritmo de Dijkstra")
plt.text(0.5, 0.95, "Resultados del Algoritmo de Dijkstra:", horizontalalignment='center', fontsize=14, transform=plt.gca().transAxes)
for node, distance in distances.items():
    path_str = []
    current_node = node
    while current_node is not None:
        path_str.append(current_node)
        current_node = path[current_node]
    path_str.reverse()
    plt.text(0.5, 0.9 - 0.05 * list(distances.keys()).index(node), f"Distancia mínima desde {start_node} a {node}: {distance}", horizontalalignment='center', fontsize=12, transform=plt.gca().transAxes)
    plt.text(0.5, 0.88 - 0.05 * list(distances.keys()).index(node), f"Camino: {' -> '.join(path_str)}", horizontalalignment='center', fontsize=12, transform=plt.gca().transAxes)

plt.axis('off')
plt.show()
