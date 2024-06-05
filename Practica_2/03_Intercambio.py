# Miguel Angel Huerta Castillo
# Registro: 21310236

# Algoritmo de Ordenamiento por Intercambio (Bubble Sort)
# Descripción: El algoritmo de ordenamiento por intercambio, también conocido como Bubble Sort, 
# funciona comparando pares de elementos adyacentes en una lista y los intercambia si están en el orden incorrecto. 
# Este proceso se repite hasta que la lista está completamente ordenada. 
# Aunque es simple de entender y fácil de implementar, es ineficiente para listas grandes 
# debido a su complejidad de tiempo O(n^2).

def bubble_sort(arr):
    n = len(arr)  # Obtener la longitud de la lista
    # Iterar a través de todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están ordenados, no es necesario revisarlos
        for j in range(0, n-i-1):
            # Comparar el elemento actual con el siguiente
            if arr[j] > arr[j+1]:
                # Si el elemento actual es mayor, intercambiar los elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Intercambio usando una asignación múltiple
    return arr  # Devolver la lista ordenada

# Ejemplo práctico
lista = [64, 34, 25, 12, 22, 11, 90]  # Lista de ejemplo para ordenar
print("Lista original:", lista)
lista_ordenada = bubble_sort(lista)  # Ordenar la lista usando Bubble Sort
print("Lista ordenada:", lista_ordenada)
