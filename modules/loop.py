import cython

def loop(n: cython.long) -> cython.void:
    i: cython.long = 1
    result: cython.longlong = 0

    for i in range(1, n + 1):
        result += i

    print(result)
