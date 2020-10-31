from math import sqrt
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y
#This function multiples two numbers
def mult(x,y):
	return x*y
#This function divides two numbers 
def div(x,y):
	return x/y
#This function gives the squareroot of a number
def squareroot(x):
	return sqrt(x)	

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. SquareRoot")
print("6. Power")
print("\n")

while True:
    # Take input from the user
    choice = input("Select choice(1/2/3/4/5/6): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6'):

        if choice == '1':
        	num1 = float(input("Enter first number: "))
       		num2 = float(input("Enter second number: "))
       		print(str(num1), "+", str(num2), "=", str(add(num1, num2)))

        elif choice == '2':
        	num1 = float(input("Enter first number: "))
        	num2 = float(input("Enter second number: "))
        	print(str(num1), "-", str(num2), "=", str(subtract(num1, num2)))

        elif choice == '3':
        	num1 = float(input("Enter first number: "))
        	num2 = float(input("Enter second number: "))
        	print(str(num1), "*", str(num2), "=", str(mult(num1, num2)))
            
        elif choice == '4':
        	num1 = float(input("Enter first number: "))
        	num2 = float(input("Enter second number: "))
        	print(str(num1), "/", str(num2), "=", str(div(num1, num2)))
        
        elif choice == "5":
        	num1 = float(input("Enter the number: "))
        	print("SqareRoot of " + str(num1) + " is " + str(sqrt(num1)))

        elif choice == "6":
        	num1 = float(input("Enter base number: "))
        	num2 = float(input("Enter power number: "))
        	print(str(num1) + " power " + str(num2) + " =" + " "+str(num1 ** num2))
        break
    else: 
        print("Invalid Input")
