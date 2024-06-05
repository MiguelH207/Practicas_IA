# Miguel Angel Huerta Castillo
# Registro: 21310236

# Ordenamiento de Árbol (Tree Sort)
# Descripción: El ordenamiento de árbol utiliza un árbol binario de búsqueda (BST) para ordenar los elementos.
# Primero, inserta todos los elementos del array en un BST. Luego, realiza un recorrido en orden del BST
# para obtener los elementos en orden ascendente. La inserción en un BST toma O(log n) en promedio, 
# y el recorrido en orden toma O(n).

class TreeNode:
    def __init__(self, key):
        self.left = None  # Hijo izquierdo
        self.right = None # Hijo derecho
        self.val = key    # Valor del nodo

def insert(root, key):
    # Si el árbol está vacío, devolver un nuevo nodo
    if root is None:
        return TreeNode(key)
    
    # De lo contrario, recorrer el árbol
    if key < root.val:
        # Insertar en el subárbol izquierdo
        root.left = insert(root.left, key)
    else:
        # Insertar en el subárbol derecho
        root.right = insert(root.right, key)
    
    # Devolver el nodo raíz sin cambios
    return root

def inorder_traversal(root, result):
    if root:
        # Recorrer el subárbol izquierdo
        inorder_traversal(root.left, result)
        # Visitar el nodo raíz
        result.append(root.val)
        # Recorrer el subárbol derecho
        inorder_traversal(root.right, result)

def tree_sort(arr):
    if not arr:
        return []
    
    # Crear el árbol binario de búsqueda e insertar el primer elemento
    root = TreeNode(arr[0])
    
    # Insertar el resto de los elementos
    for key in arr[1:]:
        insert(root, key)
    
    # Realizar el recorrido en orden
    sorted_array = []
    inorder_traversal(root, sorted_array)
    
    return sorted_array

# Ejemplo práctico
arr = [5, 3, 8, 4, 2, 7, 1, 10, 9, 6]
print("Array original:", arr)

sorted_arr = tree_sort(arr)
print("Array ordenado:", sorted_arr)
