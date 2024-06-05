# Miguel Angel Huerta Castillo
# Registro: 21310236

# Polyphase Sort
# Ordenamiento polifásico que utiliza fases y corridas para ordenar datos
# de manera eficiente en memoria externa.

def polyphase_sort(data):
    # Dividir los datos en fases y corridas iniciales
    fases = []
    fases.append([data[0]])  # La primera fase comienza con el primer elemento

    for i in range(1, len(data)):
        added = False
        # Intentar agregar el elemento a una fase existente
        for fase in fases:
            if data[i] >= fase[-1]:
                fase.append(data[i])
                added = True
                break
        # Si no se pudo agregar a ninguna fase existente, crear una nueva fase
        if not added:
            fases.append([data[i]])

    # Fusionar las fases de manera ordenada
    sorted_data = []
    current_runs = [0] * len(fases)  # Indice para seguir las corridas de cada fase

    while any(current_runs[j] < len(fases[j]) for j in range(len(fases))):
        min_value = float('inf')
        min_index = -1

        # Encontrar el mínimo de los elementos en las posiciones actuales de cada fase
        for j in range(len(fases)):
            if current_runs[j] < len(fases[j]) and fases[j][current_runs[j]] < min_value:
                min_value = fases[j][current_runs[j]]
                min_index = j

        # Agregar el mínimo al resultado ordenado y avanzar el índice de la fase correspondiente
        sorted_data.append(min_value)
        current_runs[min_index] += 1

    return sorted_data

# Ejemplo de uso
if __name__ == "__main__":
    data = [12, 4, 7, 10, 3, 5, 15, 9, 2, 11, 6, 1, 8, 14, 13]
    print("Datos sin ordenar:", data)
    sorted_data = polyphase_sort(data)
    print("Datos ordenados:", sorted_data)
