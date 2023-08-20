def NSD(a, b):
	while b:
		temp = a % b
		a = b
		b = temp
	return a

def NSK(a, b):
	return (a * b) // NSD(a, b)

fir_number = int(input("Enter first number: "))
sec_number = int(input("Enter second number: "))
print(f"NSK({fir_number},{sec_number}) = ", NSK(fir_number, sec_number))