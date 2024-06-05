# Miguel Angel Huerta Castillo
# Registro: 21310236

# Natural Merging Sort
# Este algoritmo de ordenamiento aprovecha secuencias ordenadas en el arreglo para
# reducir el número de comparaciones y fusiones necesarias. Primero identifica y 
# fusiona las subsecuencias ordenadas (runs), y luego las combina en un solo arreglo ordenado.

def natural_merge_sort(arr):
    # Función para dividir el arreglo en runs (subsecuencias ordenadas)
    def find_runs(arr):
        runs = []
        current_run = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] >= arr[i-1]:
                current_run.append(arr[i])
            else:
                runs.append(current_run)
                current_run = [arr[i]]
        
        runs.append(current_run)
        return runs
    
    # Función para fusionar dos runs ordenados
    def merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    # Obtener runs iniciales
    runs = find_runs(arr)
    
    # Mientras haya más de un run, fusionar
    while len(runs) > 1:
        merged_runs = []
        i = 0
        
        while i < len(runs) - 1:
            merged_runs.append(merge(runs[i], runs[i+1]))
            i += 2
        
        if i == len(runs) - 1:
            merged_runs.append(runs[-1])
        
        runs = merged_runs
    
    return runs[0] if runs else []

# Ejemplo de uso
if __name__ == "__main__":
    arr = [12, 4, 7, 2, 9, 1, 5, 3, 8, 6, 10, 11]
    print("Arreglo antes de ordenar:", arr)
    arr_sorted = natural_merge_sort(arr)
    print("Arreglo ordenado:", arr_sorted)
