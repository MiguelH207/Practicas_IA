# Miguel Angel Huerta Castillo
# Registro: 21310236

import tkinter as tk
from tkinter import scrolledtext, messagebox
import matplotlib.pyplot as plt
import networkx as nx

# Definir la función para el algoritmo de Prim
def prim_algorithm(vertices, matriz_costos):
    n = len(vertices)
    # Inicializar el árbol de expansión mínima y la lista de vértices visitados
    A = []
    visited = [False] * n
    visited[0] = True  # Empezamos desde el primer vértice
    
    # Ciclo principal del algoritmo
    while len(A) < n - 1:
        min_edge = None
        min_cost = float('inf')
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and matriz_costos[i][j] < min_cost:
                        min_cost = matriz_costos[i][j]
                        min_edge = (i, j)
        
        if min_edge:
            u, v = min_edge
            A.append((u, v))
            visited[v] = True
    
    return A

# Función para imprimir los pasos del algoritmo en la consola
def imprimir_pasos(vertices, arbol):
    print("Árbol de Expansión Mínima de Prim:")
    total_cost = 0
    for u, v in arbol:
        total_cost += matriz_costos[u][v]
        print(f"Arista: {vertices[u]} - {vertices[v]}, Costo: {matriz_costos[u][v]}")
    print(f"Costo total del árbol: {total_cost}")

# Datos de ejemplo
vertices = ['A', 'B', 'C', 'D']
matriz_costos = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]

# Ejecutar el algoritmo de Prim
arbol_minimo = prim_algorithm(vertices, matriz_costos)

# Mostrar pasos en la consola
imprimir_pasos(vertices, arbol_minimo)

# Crear el gráfico del grafo y el árbol de expansión mínima con matplotlib y networkx
G = nx.Graph()
G.add_nodes_from(vertices)
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        if matriz_costos[i][j] > 0:
            G.add_edge(vertices[i], vertices[j], weight=matriz_costos[i][j])

# Crear el árbol de expansión mínima
T = nx.Graph()
T.add_nodes_from(vertices)
T.add_edges_from([(vertices[u], vertices[v]) for u, v in arbol_minimo])

# Obtener posiciones de los nodos para la visualización
pos = nx.spring_layout(G)

# Interfaz gráfica con tkinter y matplotlib
root = tk.Tk()
root.title("Simulador de Árbol de Expansión Mínima de Prim")

# Crear un área de texto para mostrar los resultados
text_area = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_area.insert(tk.INSERT, "Árbol de Expansión Mínima de Prim:\n")
for u, v in arbol_minimo:
    text_area.insert(tk.INSERT, f"Arista: {vertices[u]} - {vertices[v]}, Costo: {matriz_costos[u][v]}\n")
text_area.insert(tk.INSERT, f"Costo total del árbol: {sum(matriz_costos[u][v] for u, v in arbol_minimo)}\n")
text_area.pack(side=tk.BOTTOM)

# Función para mostrar el grafo y el árbol en la interfaz
def mostrar_grafo():
    fig, ax = plt.subplots()
    nx.draw_networkx(G, pos=pos, with_labels=True, ax=ax, node_color='lightblue', node_size=800, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(T, pos=pos, ax=ax, edgelist=T.edges(), width=2, edge_color='orange')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels={(u, v): matriz_costos[vertices.index(u)][vertices.index(v)] for u, v in G.edges()}, ax=ax, font_color='red')
    ax.set_title('Grafo y Árbol de Expansión Mínima de Prim')
    plt.show()

# Botón para mostrar el grafo en la interfaz
button_show_graph = tk.Button(root, text="Mostrar Grafo", command=mostrar_grafo)
button_show_graph.pack(side=tk.TOP)

root.mainloop()
