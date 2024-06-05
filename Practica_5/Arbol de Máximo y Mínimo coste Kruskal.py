# Autor: Miguel Angel Huerta Castillo
# Registro: 21310236
# 
# Título: Simulador de Algoritmo de Árbol de Máximo y Mínimo Costo - Kruskal
#
# Descripción:
# El algoritmo de Kruskal es un método para encontrar el árbol de expansión mínima en un grafo conectado y no dirigido.
# Este algoritmo selecciona las aristas en orden ascendente de peso y las añade al árbol de expansión mínima, asegurándose
# de que no se formen ciclos. Al final, se obtiene un subgrafo que conecta todos los nodos con el costo mínimo.


import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class KruskalSimulator:
    def __init__(self):
        # Inicializa la interfaz gráfica
        self.root = tk.Tk()
        self.root.title("Simulador de Kruskal")
        
        # Etiquetas y entradas para los nodos y aristas
        self.label_nodes = tk.Label(self.root, text="Nodos (separados por comas):")
        self.label_nodes.pack()
        self.entry_nodes = tk.Entry(self.root)
        self.entry_nodes.insert(0, "A,B,C,D,E")
        self.entry_nodes.pack()

        self.label_edges = tk.Label(self.root, text="Aristas (formato: nodo1,nodo2,peso):")
        self.label_edges.pack()
        self.entry_edges = tk.Entry(self.root)
        self.entry_edges.insert(0, "A,B,1 B,C,2 C,D,3 D,E,4 E,A,5 A,C,6")
        self.entry_edges.pack()
        
        # Botón para iniciar el algoritmo
        self.button = tk.Button(self.root, text="Ejecutar Kruskal", command=self.run_kruskal)
        self.button.pack()
        
        self.root.mainloop()
    
    def run_kruskal(self):
        # Obtiene los nodos y las aristas de las entradas de texto
        nodes = self.entry_nodes.get().split(',')
        edges = self.entry_edges.get().split()
        
        # Parsea las aristas
        edges = [tuple(edge.split(',')) for edge in edges]
        edges = [(edge[0], edge[1], int(edge[2])) for edge in edges]
        
        # Crea el grafo
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_weighted_edges_from(edges)
        
        # Ejecuta el algoritmo de Kruskal
        mst = self.kruskal(G)
        
        # Muestra los resultados
        self.show_result(G, mst)
    
    def kruskal(self, G):
        # Ordena las aristas por peso
        edges = sorted(G.edges(data=True), key=lambda t: t[2]['weight'])
        
        # Inicializa el árbol de expansión mínima
        mst = nx.Graph()
        
        # Diccionario para realizar la unión y búsqueda de conjuntos
        parent = {node: node for node in G.nodes()}
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root2] = root1
        
        # Agrega las aristas al árbol de expansión mínima
        for u, v, data in edges:
            if find(u) != find(v):
                mst.add_edge(u, v, weight=data['weight'])
                union(u, v)
        
        return mst
    
    def show_result(self, G, mst):
        # Dibuja el grafo original
        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Grafo Original")
        plt.show()
        
        # Dibuja el árbol de expansión mínima
        plt.figure()
        nx.draw(mst, pos, with_labels=True, node_color='lightgreen', edge_color='red')
        labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
        plt.title("Árbol de Expansión Mínima (Kruskal)")
        plt.show()

if __name__ == "__main__":
    KruskalSimulator()
