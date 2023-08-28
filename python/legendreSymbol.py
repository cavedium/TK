def module(a, b):
    return a % b

def NSD(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return a

def legendreSymbol(a, p):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        if module(p, 8) == 1 or module(p, 8) == 7:
            return 1
        else:
            return -1
    if a>= p:
        return legendreSymbol(a % p, p)
    if module(a, 2) == 0:
        if module(p, 8) == 1 or module(p, 8) == 7:
            return legendreSymbol(a / 2, p)
        else: 
            return -legendreSymbol(a / 2, p)
    if NSD(a, p) != 1:
        return 0
    if module(a, 4) == 3 and module(p, 2) == 3:
        return -legendreSymbol(p, a)
    else:
        return legendreSymbol(p, a)

a = int(input("Enter number: "))
p = int(input("Enter second number: "))

print(f"Legendre Symbol is {legendreSymbol(a, p)}")