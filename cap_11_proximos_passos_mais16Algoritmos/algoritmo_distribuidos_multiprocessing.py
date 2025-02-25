from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as p:
    print(p.map(square, [1, 2, 3, 4, 5]))
