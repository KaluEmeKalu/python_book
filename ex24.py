num1 = input("Please type the first number: ")
num2 = input("Please type the second number: ")
num3 = input("Please type the third number: ")
num4 = input("Please type the forth number: ")
numbers = [num1, num2, num3, num4]

for num in numbers:
	if num % 2 == 0:
		print("The number " + str(num) + " is even")
	else:
		print("The number " + str(num) + " is odd")