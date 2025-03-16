import matplotlib.pyplot as plt
import numpy as np
from palindrome import execution_time_gathering


def choose_algortihms():
    print("""Please enter the algorithms to test:
    1. Two Pointers
    2. Reversed
    3. Recursive
    4. Stack""")
    algorithms = list(map(int, input().split()))
    algorithmsNames = ["Two Pointers", "Reversed", "Recursive", "Stack"]

    print("Enter the minimum size of the strings to test:")
    minimum_size = int(input())
    
    print("Enter the maximum size of the strings to test:")
    maximum_size = int(input())

    print("Enter the step: ")
    step = int(input())

    print("Enter the amount of samples by size: ")
    samples_by_size = int(input())

    data = execution_time_gathering.take_execution_time_choose(minimum_size, maximum_size, step, 
                                                               samples_by_size, algorithms)
    
    j = 1
    sizes = [row[0] for row in data]
    for i in algorithms:
        times = [row[j] for row in data]
        plt.scatter(sizes, times, label=algorithmsNames[i-1])
        plt.plot(sizes, times)
        j += 1

    plt.xlabel("Tamaño de los datos")
    plt.ylabel("Tiempo de ejecución en ms")
    plt.title("Comparación algoritmos de decisión de palíndromos")

    plt.legend()

    plt.show()

choose_algortihms()