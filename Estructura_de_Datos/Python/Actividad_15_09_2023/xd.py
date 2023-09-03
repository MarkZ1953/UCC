def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
