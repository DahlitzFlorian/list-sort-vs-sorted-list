import random
import resource
import sys
import time

from sniffing import FunctionSniffingClass


def list_sort(arr):
    return arr.sort()


def sorted_builtin(arr):
    return sorted(arr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Please run: python (sort|sorted)")
    elif sys.argv[1] == "sorted":
        func = sorted_builtin
    elif sys.argv[1] == "sort":
        func = list_sort
    else:
        sys.exit("Please run: python (sort|sorted)")

    # Lib Testing Code
    arr = [random.randint(0, 50) for r in range(1_000_000)]
    mythread = FunctionSniffingClass(func, arr)
    mythread.start()

    used_mem = 0
    max_memory = 0
    memory_usage_refresh = 0.005  # Seconds

    while 1:
        time.sleep(memory_usage_refresh)
        used_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if used_mem > max_memory:
            max_memory = used_mem

        # Check to see if the function call is complete
        if mythread.isShutdown():
            # Uncomment if yu want to see the results
            # print(mythread.results)
            break

    print("\nMAX Memory Usage:", round(max_memory / (2 ** 20), 3), "MB")
