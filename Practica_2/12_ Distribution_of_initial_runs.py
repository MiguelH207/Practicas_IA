# Datos del usuario
# Miguel Angel Huerta Castillo   registro:21310236

# Título del ordenamiento: Distribution of Initial Runs (Ordenamiento por distribución de carreras iniciales)
# Descripción: Este algoritmo divide el arreglo en carreras (runs), las ordena internamente y luego las fusiona para obtener el arreglo ordenado.

def distribution_of_initial_runs(arr):
    def merge(arr, l, m, r):
        # Función auxiliar para fusionar dos subarreglos ordenados
        left_half = arr[l:m+1]
        right_half = arr[m+1:r+1]

        i = j = 0
        k = l

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    n = len(arr)
    size = 1

    # Divide el arreglo en carreras (runs), las ordena y las fusiona
    while size < n:
        left = 0
        while left < n - 1:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            merge(arr, left, mid, right)

            left += 2 * size

        size *= 2

# Ejemplo de uso
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Arreglo original:", arr)
    
    distribution_of_initial_runs(arr)
    
    print("Arreglo ordenado:", arr)
