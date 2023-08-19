def module(a, b):
    return a % b

num = int(input("Enter number: "))
mod = int(input("Enter module: "))
print(f"{num}mod{mod} = ", module(num, mod))