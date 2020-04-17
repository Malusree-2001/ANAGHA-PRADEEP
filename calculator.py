# Program make a simple calculator

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

print("Select operation.")
print("1.Add")
print("2.Subtract")

# Take input from the user 
choice = input("Enter choice(1/2): ")

first_number = float(input("Enter first number: "))
second_number= float(input("Enter second number: "))

if choice == '1':
   print(first_number,"+",second_number,"=", add(first_number,second_number))

elif choice == '2':
   print(first_number,"-",second_number,"=", subtract(first_number,second_number))

else:
   print("Invalid input")


