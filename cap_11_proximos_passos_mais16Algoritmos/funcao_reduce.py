from functools import reduce

data = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, data)
print(result)
