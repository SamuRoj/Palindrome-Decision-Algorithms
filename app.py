import sys
from palindrome import algorithms
from palindrome import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 5000
    step = 1000
    samples_by_size = 100

    sys.setrecursionlimit(5000)
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Two Pointers | Reverse String | Recursive | Stack ")
    for row in table:
        print(row)
