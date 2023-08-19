def NSD(a, b):
	while b:
		temp = a % b
		a = b
		b = temp
	return a

fir_number = int(input("Enter first number: "))
sec_number = int(input("Enter second number: "))
print(f"NSD({fir_number},{sec_number}) = ", NSD(fir_number, sec_number))
