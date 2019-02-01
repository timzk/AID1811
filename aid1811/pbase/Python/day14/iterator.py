L = [2,3,5,7]
it = iter(L)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

