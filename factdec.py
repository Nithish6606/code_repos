import time
'''-----------------------------------------------------------------------'''
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        ex_time=end - start
        print(f"{func.__name__} executes {ex_time:.5f} sec`s")
        return result
    return wrapper
'''------------------------------------------------------------------------'''
def fact(n:int)->int:
    if n==0:
        return 1
    else:
        return n*fact(n-1)
@timer    
def print_fact(n:int)->None:
    result=fact(n)
    print(f'The Factorial of {n} is {result}')

def main()->None:
    num:int=int(input("Enter the number:"))
    print_fact(num)

if __name__ == '__main__':
    main()