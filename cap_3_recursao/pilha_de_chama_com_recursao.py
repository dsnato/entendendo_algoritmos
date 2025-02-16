def fat(x):
    if x == 0:
        return 1
    else:
        return x * fat(x-1)

print(fat(0))
print(fat(5))
