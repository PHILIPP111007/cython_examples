from modules.time_counter import time_counter


@time_counter
def cython_func():
    from modules.loop import loop

    loop(1_000_000_000)


cython_func()
