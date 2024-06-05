# Miguel Angel Huerta Castillo
# Registro: 21310236

# Radix Sort para manejar números positivos y negativos
# Ordenamiento por radix es un algoritmo que ordena números enteros procesando dígito por dígito, 
# desde el dígito menos significativo hasta el más significativo. Utiliza un algoritmo de 
# ordenamiento estable para distribuir los números en cubetas según el valor de los dígitos. 
# Es eficiente para ordenar números con una cantidad fija de dígitos, como por ejemplo números enteros.

def radix_sort(arr):
    # Separar los números negativos y positivos
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]
    
    # Convertir los números negativos a positivos para ordenar
    negatives = [-x for x in negatives]
    
    # Ordenar los números positivos y negativos
    positives = radix_sort_positive(positives)
    negatives = radix_sort_positive(negatives)
    
    # Invertir los números negativos a su forma original
    negatives = [-x for x in reversed(negatives)]
    
    # Combinar los resultados ordenados
    return negatives + positives

def radix_sort_positive(arr):
    # Encontrar el número máximo para determinar el número de dígitos
    max_value = max(arr)
    # Inicializar el divisor para obtener cada dígito
    divisor = 1
    
    # Mientras haya dígitos para procesar
    while max_value // divisor > 0:
        # Llamar a la función de conteo para ordenar según el dígito específico
        arr = counting_sort(arr, divisor)
        # Incrementar el divisor para moverse al siguiente dígito
        divisor *= 10
    
    return arr

def counting_sort(arr, divisor):
    # Inicializar la lista de cubetas para contar las ocurrencias de cada dígito
    count = [0] * 10
    # Inicializar la lista de salida que contendrá los elementos ordenados
    output = [0] * len(arr)
    
    # Contar las ocurrencias de cada dígito en el array dado
    for num in arr:
        digit = (num // divisor) % 10
        count[digit] += 1
    
    # Ajustar la lista de conteo para tener las posiciones finales de los dígitos
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el array de salida utilizando la lista de conteo
    i = len(arr) - 1
    while i >= 0:
        digit = (arr[i] // divisor) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1
    
    return output

# Ejemplo de uso
if __name__ == "__main__":
    arr = [170, -45, 75, -90, 802, -24, 2, 66]
    print("Array original:", arr)
    sorted_arr = radix_sort(arr)
    print("Array ordenado:", sorted_arr)
