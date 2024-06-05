# Miguel Angel Huerta Castillo
# Registro: 21310236

# Selection Sort
# El algoritmo de ordenamiento por selección funciona dividiendo el array en una parte ordenada y otra no ordenada.
# En cada iteración, encuentra el elemento mínimo de la parte no ordenada y lo intercambia con el primer elemento de la parte no ordenada.
# Esto incrementa la parte ordenada y reduce la parte no ordenada hasta que todo el array está ordenado.

def selection_sort(arr):
    # Recorremos todo el array
    for i in range(len(arr)):
        # Encontramos el índice del elemento mínimo en la sublista no ordenada
        min_idx = i
        for j in range(i + 1, len(arr)):
            # Si encontramos un elemento menor, actualizamos min_idx
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el elemento mínimo encontrado con el primer elemento de la sublista no ordenada
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo práctico
# Definimos un array desordenado
example_array = [64, 25, 12, 22, 11]

# Imprimimos el array original
print("Array original:", example_array)

# Ordenamos el array utilizando Selection Sort
sorted_array = selection_sort(example_array)

# Imprimimos el array ordenado
print("Array ordenado:", sorted_array)
