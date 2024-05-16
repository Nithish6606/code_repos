import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        ex_time=end - start
        print(f"{func.__name__} executes {ex_time:.5f} sec`s")
        return result
    return wrapper
def memorize(func):
    cache={}
    def wrapper(*args,**kwargs):
        key=(args,tuple(kwargs.items()))
        if key not in cache:
            cache[key]=func(*args,**kwargs)
        return cache[key]
    return wrapper
'''------------------------------------------------------------------------'''
@memorize
def fib(n:int)->int:
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
@timer
def print_fib(n:int)->None:
    result=fib(n)
    print(f"The Fibonacci of {n} is {result}")

def main()->None:
    num:int=int(input("Enter the number:"))
    print_fib(num)

if __name__ == '__main__':
    main()