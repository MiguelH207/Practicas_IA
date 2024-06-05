# Miguel Angel Huerta Castillo
# Registro: 21310236

# Algoritmo de Ordenamiento Rápido (QuickSort)

# Descripción:
# QuickSort es un algoritmo de ordenamiento basado en el principio de "divide y vencerás".
# El algoritmo selecciona un elemento llamado "pivote" y reordena el array de manera que 
# todos los elementos menores que el pivote estén a la izquierda y todos los elementos 
# mayores estén a la derecha. Luego, aplica recursivamente el mismo proceso a las sublistas 
# izquierda y derecha.

def quicksort(arr):
    """
    Función principal de QuickSort que ordena un array.

    Args:
    arr (list): Lista de elementos a ordenar.

    Returns:
    list: Lista ordenada.
    """
    # Caso base: si el array tiene 1 o menos elementos, ya está ordenado.
    if len(arr) <= 1:
        return arr

    # Elegimos el pivote. En este caso, elegimos el elemento del medio.
    pivot = arr[len(arr) // 2]

    # Sublistas para almacenar elementos menores, iguales y mayores que el pivote.
    left = [x for x in arr if x < pivot]  # Elementos menores que el pivote.
    middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote.
    right = [x for x in arr if x > pivot]  # Elementos mayores que el pivote.

    # Llamamos recursivamente a quicksort para ordenar las sublistas izquierda y derecha,
    # y concatenamos los resultados con la sublista del pivote.
    return quicksort(left) + middle + quicksort(right)

# Ejemplo práctico:
array = [33, 10, 55, 71, 29, 23, 87, 42]
print("Array original:", array)
sorted_array = quicksort(array)
print("Array ordenado:", sorted_array)

# Salida esperada:
# Array original: [33, 10, 55, 71, 29, 23, 87, 42]
# Array ordenado: [10, 23, 29, 33, 42, 55, 71, 87]
