def add(a,b):
	result=a+b
	print(result)
def subtract(a,b):
	result=a-b
	print(result)
def multiply(a,b):
	result=a*b
	print(result)
def divide(a,b):
	result=a/b
	print(result)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operation=input("Enter the operator: ")

if operation=="+":
	add(a,b)
elif operation=="-":
	subtract(a,b)
elif operation=="*":
	multiply(a,b)
elif operation=="/":
	divide(a,b)
else:
	print("Invalid entry! Please try again.")