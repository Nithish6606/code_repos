def greet(name:str)->str:
    return f"Hello, {name}!"
def main()->None:
    name:str=input("Enter the name:")
    print(greet(name))

if __name__ == "__main__":
    main()