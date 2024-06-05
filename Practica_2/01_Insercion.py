# Miguel Angel Huerta Castillo
# Registro: 21310236
# Insercion
# Construye el array ordenado de uno en uno, insertando cada nuevo elemento en su posición correcta.

def insertion_sort(arr):
    # Recorremos el array desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Almacenamos el valor del elemento actual
        key = arr[i]
        # Inicializamos la variable j como el índice anterior al actual
        j = i - 1
        # Movemos los elementos del array que son mayores que la clave
        # a una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Colocamos la clave en su posición correcta
        arr[j + 1] = key

# Ejemplo 
arr = [12, 11, 13, 5, 6]

print("Array original:", arr)
# Llamamos a la función de ordenamiento por inserción
insertion_sort(arr)
print("Array ordenado:", arr)
