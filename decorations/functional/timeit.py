import time

def timeit(return_time=False):
    """Decorator to time a function."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if return_time:
                return result, elapsed_time
            else:
                print("Function {} took {} seconds".format(func.__name__,elapsed_time))
                return result
        return wrapper
    return decorator