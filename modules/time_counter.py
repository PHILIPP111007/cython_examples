import cython


def time_counter(func):
    def wrapper(*args, **kwargs) -> cython.void:
        import time

        start: cython.double = time.time()
        func(*args, **kwargs)
        end: cython.double = time.time()

        print(f"{func}: {end - start} sec")

    return wrapper
