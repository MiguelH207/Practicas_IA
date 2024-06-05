# Miguel Angel Huerta Castillo
# Registro: 21310236

# Algoritmo de Merge Sort (Ordenamiento por mezcla)
# Descripción:
# Merge Sort es un algoritmo de ordenamiento que sigue el principio de "divide y vencerás". 
# Primero divide el array en dos mitades, luego ordena cada mitad de forma recursiva, 
# y finalmente combina (merge) las dos mitades ordenadas en un solo array ordenado.

def merge_sort(arr):
    # Si el array tiene más de un elemento, lo dividimos en dos mitades
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio del array
        left_half = arr[:mid]  # Dividimos la primera mitad
        right_half = arr[mid:]  # Dividimos la segunda mitad

        # Llamamos recursivamente a merge_sort en ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializamos índices para recorrer las sublistas
        i = j = k = 0

        # Combinamos las dos mitades ordenadas en un solo array ordenado
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Comprobamos si quedaron elementos en la mitad izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Comprobamos si quedaron elementos en la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ejemplo práctico:
array = [38, 27, 43, 3, 9, 82, 10]

print("Array original:", array)
merge_sort(array)
print("Array ordenado:", array)
