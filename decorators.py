import time
#from functools import cache
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.2f} seconds to execute")
        return result
    return wrapper

def cache(inner_func):
    results = {}

    def wrapped_func(k: any):
        if k not in results:
            results[k] = inner_func(k)
        return results[k]

    return wrapped_func

@cache
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
def print_fibonacci(n: int):
    result = fibonacci(n)
    print(result)

def main()->None:
    print_fibonacci(60)

if __name__ == "__main__":
    main()