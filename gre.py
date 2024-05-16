def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def greet(name:str)->str:
    return f"Hello, {name}!"
def main()->None:
    name:str=input("Enter the name:")
    print(greet(name))

if __name__ == "__main__":
    main()