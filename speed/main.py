# speed/main.py

import random

from boxx import timeit


def list_sort(arr):
    return arr.sort()


def sorted_builtin(arr):
    return sorted(arr)


def main():
    arr = [random.randint(0, 50) for r in range(1_000_000)]

    with timeit(name="sorted(list)"):
        sorted_builtin(arr)

    with timeit(name="list.sort()"):
        list_sort(arr)


if __name__ == "__main__":
    main()
