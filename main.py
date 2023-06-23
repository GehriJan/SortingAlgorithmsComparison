# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import array as arr
import time
import numpy as np
import matplotlib.pyplot as plt
import random


# todo zeitmessung einfügen mit tabelle
# todo zufällige arrays und überprüfung, ob Sortierung stimmt
# todo Insertion Sort implementieren
# todo QuickSort implementieren


# EINFACH
def selectionSort(array):
    for i in range(0, len(array)):
        minVal = array[i]
        minPos = i
        for j in range(i, len(array)):
            if (array[j] < minVal):
                minVal = array[j]
                minPos = j
        array[minPos] = array[i]
        array[i] = minVal
    return array


def insertionSort(array):
    for i in range(1, len(array)):
        k = i
        for j in range(i - 1, -1, -1):
            if array[j] > array[k]:
                array[j], array[k] = array[k], array[j]
            k -= 1
    return array


def bubbleSort(array):
    for i in range(0, len(array)):
        k = 0
        for j in range(k + 1, len(array) - i):
            if array[k] > array[j]:
                array[j], array[k] = array[k], array[j]
            k += 1
    return array


# REKURSIV
def mergeSort(array):
    # todo mergesort nochmal überarbeiten

    if len(array) <= 1: return array

    lArr = array[int(len(array) / 2):]
    rArr = array[:int(len(array) / 2)]

    lArr = mergeSort(lArr)
    rArr = mergeSort(rArr)

    lCtr = 0
    rCtr = 0
    mergedArray = [0] * len(array)
    for i in range(0, len(array)):
        if rCtr == len(rArr):
            mergedArray[i] = lArr[lCtr]
            lCtr += 1
        elif lCtr == len(lArr):
            mergedArray[i] = rArr[rCtr]
            rCtr += 1
        else:
            if lArr[lCtr] <= rArr[rCtr]:
                mergedArray[i] = lArr[lCtr]
                lCtr += 1
            else:
                mergedArray[i] = rArr[rCtr]
                rCtr += 1
    return mergedArray


# VON VORLESUNG
def heapify(array):
    end = len(array)
    last = (end - 1) // 2
    # last inner node
    for node in range(last, -1, -1):
        bubbledown(arr, node, end)
    return


def heapsort(array):
    last = len(array) - 1
    heapify(array)
    for i in range(last, 0, -1):
        array[0], array[i] = array[i], array[0]
        bubbledown(array, 0, i)
    return array


def bubbledown(array, node, end):
    lci = 2 * node + 1
    if lci < end:
        gci = lci
        rci = lci + 1
        if rci < end:
            if array[rci] > array[lci]:
                gci = rci
        if array[gci] > array[node]:
            array[node], array[gci] = array[gci], array[node]
            bubbledown(array, gci, end)
    return


# CHATGPT
def quickSortChatGPT(array):
    quickArray = array
    left = 0
    right = len(quickArray) - 1
    stack = [(left, right)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = quickArray[left]
        i, j = left + 1, right
        while i <= j:
            while i <= j and quickArray[i] <= pivot:
                i += 1
            while i <= j and quickArray[j] >= pivot:
                j -= 1
            if i < j:
                quickArray[i], quickArray[j] = quickArray[j], quickArray[i]

        quickArray[left], quickArray[j] = quickArray[j], quickArray[left]

        if j - left <= right - j - 1:
            stack.append((j + 1, right))
            stack.append((left, j - 1))
        else:
            stack.append((left, j - 1))
            stack.append((j + 1, right))

    return quickArray


def mergeSortChatGPT(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return np.array(merged)

# MESSUNGSFUNKTIONEN
def measure(func):
    array2 = array1
    prevTime = time.time()
    func(array2)
    return 1000 * (time.time() - prevTime)


def plot():
    for algorithm in sortingAlgos:
        plt.scatter(ctrElements, algoArrDic[algorithm.__name__], label=algorithm.__name__)
    plt.suptitle("Laufzeitvergleich", fontsize=14, fontweight="bold")
    plt.title(
        "Anzahl Messungen: " + str(anzPoints - 1) + "   Schrittgröße: " + str(stepSize) + "   MaxRand: " + str(maxRand))
    plt.xlabel("n")
    plt.ylabel("Laufzeit in ms")
    plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    anzPoints = 20
    stepSize = 1000
    maxRand = 1000
    sortingAlgos = [quickSortChatGPT, mergeSort, bubbleSort]
    times = []
    ctrElements = [0]
    algoArrDic = {}

    for i in range(1, anzPoints):
        array1 = [random.randint(0, maxRand) for _ in range(stepSize * i)]
        for algorithm in sortingAlgos:
            if i == 1:
                algoArrDic[algorithm.__name__] = [0.0]
            algoArrDic[algorithm.__name__].append(measure(algorithm))
            if i == anzPoints - 1:
                print(algorithm.__name__)
                print(algorithm(array1))
        ctrElements.append(stepSize * i)
    plot()

#     print("Insertionsort: " + insertionSort(array))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
