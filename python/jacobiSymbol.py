def module(a, b):
    return a % b

def jacobi_symbol(a, b):
    result = 1
    while a != 0:
        while module(a, 2) == 0:
            a /= 2
            if module(b, 8) == 3 or module(b, 8) == 5:
                result = -result
        temp = a
        a = b
        b = temp
        if module(a, 4) == 3 and module(b, 4) == 3:
            result = -result
        a = module(a, b)
    if b == 1:
        return result
    return 0

a = int(input("Enter number: "))
p = int(input("Eter prime number p: "))

print(f"Jacobi symbol for a number {a} and module {p} = {jacobi_symbol(a, p)}")