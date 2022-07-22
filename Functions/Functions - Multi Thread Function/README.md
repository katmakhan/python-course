# Multi Thread

Using Threadpool for running same function with multiple inputs simultaneously

### Import Function
```python
from multiprocessing.pool import ThreadPool
```

### Initialise the pool size
Put n = any number of threads you would like to execute simultaneously
```python
pool=ThreadPool(n)
```

### Start the pool Function
- One Argument Functions

```python
#using pool.map for 1 argument function
pool.map(function1,[("val_arg1"),("val_arg2"),("val_arg3")])
```

- Multiple Argument Functions

```python
#using pool.starmap for multiple argument function
pool.map(function1,[("val_arg1","Bval_arg1"),("val_arg2","Bval_arg2"),("val_arg3",,"Bval_arg3")])
```