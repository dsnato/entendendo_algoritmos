from functools import reduce

data = [1, 2, 3, 4, 5]

def mapper(x):
    return x * x

def reducer(x, y):
    return x + y

mapped = list(map(mapper, data))
result = reduce(reducer, mapped)
print(result)
