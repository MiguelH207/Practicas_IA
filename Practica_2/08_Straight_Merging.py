# Miguel Angel Huerta Castillo
# Registro: 21310236

# Algoritmo de Straight Merging
# Descripción: Straight Merging es un algoritmo de ordenamiento que combina dos listas ordenadas en una sola lista ordenada.
# Funciona tomando dos listas ordenadas y combinándolas de manera que los elementos se fusionen en una lista ordenada más grande.

def straight_merge(list1, list2):
    merged_list = []  # Inicializamos la lista donde almacenaremos el resultado ordenado
    i = 0  # Índice para recorrer list1
    j = 0  # Índice para recorrer list2
    
    # Combinar list1 y list2 en merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Añadir los elementos restantes de list1, si los hay
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Añadir los elementos restantes de list2, si los hay
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Ejemplo de uso:
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

merged = straight_merge(lista1, lista2)
print(f"Lista combinada ordenada: {merged}")
