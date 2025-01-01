import time


def performance_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        time_took = time.perf_counter() - start_time

        return result, round(time_took, 2)
    return wrapper