# Memory Measurement


## Description

The memory usage is measured by using the built-in [resource][resource] module.
Therefore, a `FunctionSniffingClass` was implemented to run a single function in a separate thread to be able to measure the memory of the whole thread.

**Note:** This approach may cause unrecognized overhead.

The implementations of `FunctionSniffingClass` and `StoppableThread` are modified variants of the ones published by [Adam Lewis][adamlewis] on [StackOverflow][soanswer].


## Usage

You can use the tool provided in this subdirectory as follows:

```shell
$ python main.py (sort|sorted)
```

You have two options to run this: Either with `sorted` as argument or with `sort` as argument.
Depending on which one you specify, the memory usage is measured for the `list.sort()` method or for the builtin `sorted(list)` function.


### Example Output

```shell
$ python main.py sort
Calling the Target Function...
Function Call Complete

MAX Memory Usage: 23.371 MB
```

```shell
$ python main.py sorted
Calling the Target Function...
Function Call Complete

MAX Memory Usage: 30.879 MB
```


[adamlewis]: https://stackoverflow.com/users/157744/adam-lewis
[resource]: https://docs.python.org/3/library/resource.html#resource-usage
[soanswer]: https://stackoverflow.com/a/10117657
