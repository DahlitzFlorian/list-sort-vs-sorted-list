# Speed


## Description

The speed is measured by using the third-party [boxx][boxx] module.
In particular the `timeit` function is used.
This section of the repository makes use of the same NumPy array size and value range as the other sections.


## Usage

You can use the speed test by simply running:

```shell
$ python main.py
```

This will display you the execution time of both wrapper functions.

**Note:** The `sorted_builtin` function is called first as the `list_sort` function modifies the list just in-place. If changing the order, the `sorted_builtin` function don't need to sort anything.


# Example Output

```shell
$ python main.py
"sorted(list)" spend time: 0.1104379
"list.sort()" spend time: 0.0956471
```


[boxx]: https://github.com/DIYer22/boxx
