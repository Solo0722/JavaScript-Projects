#HOW TO BUILD A SIMPLE CALCULATOR
#1.ADD
#2.SUBTRACT
#3.MULTIPLY
#4.DIVIDE

print("Select an operation to perform: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.SQUARE ROOT")

operation=input()
if operation=="1":
	a=input("Enter first number: ")
	b=input("Enter second number: ")
	result=int(a)+int(b)
	print("The sum is "+str(result))
elif operation=="2":
	a=input("Enter first number: ")
	b=input("Enter second number: ")
	result=int(a)-int(b)
	print("The difference is "+str(result))
elif operation=="3":
	a=input("Enter first number: ")
	b=input("Enter second number: ")
	result=int(a)*int(b)
	print("The product is "+str(result))
elif operation=="4":
	a=input("Enter first number: ")
	b=input("Enter second number: ")
	result=int(a)/int(b)
	print("The result is "+str(result))
elif operation=="5":
    a=input("Enter number:")
    result=int(a)*int(a)
    print("The square of "+a+ " is "+str(result))
else:
	print("Invalid entry!")


