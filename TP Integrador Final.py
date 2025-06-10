import random
import time

#Método Bubble Sort:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#Metodo Quick Sort:

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pi = particion(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def particion(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)

#Método Selection Sort:

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#Método Insertion Sort:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = actual

#Función para medir el tiempo de cada método:

def medir_tiempo(algoritmo, lista):
    copia = lista.copy()
    inicio = time.time()
    algoritmo(copia)
    fin = time.time()
    return fin - inicio

#Comparación de tiempos: 

tamaños = [100, 500, 1000]
algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Quick Sort", quick_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort)
]

for n in tamaños:
    print(f"\n📏 Tamaño de lista: {n}")
    lista = [random.randint(0, 10000) for _ in range(n)]
    for nombre, funcion in algoritmos:
        tiempo = medir_tiempo(funcion, lista)
        print(f"{nombre:<18}: {tiempo:.6f} segundos")


