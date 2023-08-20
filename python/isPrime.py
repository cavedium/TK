def isPrime(a):
    if (a <= 1):
        return False
    elif (a > 1):
        for temp in range(2, a):
            if(a % temp == 0):
                return False
    return True

number = int(input("Enter your number: "))

if isPrime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")