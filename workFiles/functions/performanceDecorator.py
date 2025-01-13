import time


def performance_decorator(func):
    total_time = 0

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        time_took_seconds = time.perf_counter() - start_time

        time_took_minutes = round(time_took_seconds / 60, 2)

        nonlocal total_time
        total_time += time_took_minutes
        print(f"Total time: {round(total_time, 2)}[min]")

        return result, time_took_minutes

    return wrapper
