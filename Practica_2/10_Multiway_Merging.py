# Miguel Angel Huerta Castillo
# Registro: 21310236

# Título: Balanced Multiway Merging
# Descripción: Balanced Multiway Merging es un algoritmo de ordenamiento externo que combina múltiples listas ordenadas en una sola lista ordenada de manera eficiente, minimizando el número de comparaciones y accesos a disco.

def balanced_multiway_merging(lists):
    """
    Función que implementa Balanced Multiway Merging para combinar múltiples listas ordenadas en una sola lista ordenada.

    Args:
    - lists: Una lista de listas, donde cada lista interna está ordenada.

    Returns:
    - merged_list: Una lista ordenada que contiene todos los elementos de las listas de entrada.
    """
    import heapq

    # Creamos un heap inicial con el primer elemento de cada lista y su índice
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]

    heapq.heapify(heap)  # Convertimos la lista en un heap mínimo

    merged_list = []
    while heap:
        val, list_index, element_index = heapq.heappop(heap)  # Obtenemos el menor elemento actual

        merged_list.append(val)  # Agregamos el elemento al resultado final

        # Obtenemos el siguiente elemento de la lista actual si existe
        if element_index + 1 < len(lists[list_index]):
            next_element = lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_element, list_index, element_index + 1))

    return merged_list

# Ejemplo de uso:
if __name__ == "__main__":
    lists = [
        [1, 3, 5],
        [2, 4, 6],
        [0, 7, 8],
    ]

    sorted_list = balanced_multiway_merging(lists)
    print("Lista ordenada resultante:", sorted_list)
