def generators(a, b):
    temp = 1
    for i in range(1, b-2):
        temp = (temp * a) % b
        if temp == 1:
            return False
    temp = (temp * a) % b
    return True

n = int(input("Enter a positive integer number: "))

for g in range(2, n):
    if generators(g, n):
        print(f"{g} is a generator of", n)
