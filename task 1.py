# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

num1 = int(input('enter a value:'))
num2 = int(input('enter a value:'))

#methematical operation
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print('addition', num1 + num2)
print('subtraction', num1 - num2)
print('multiplication',num1 * num2)
print('division', num1 / num2)


# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name

# Get user's first name
first_name = input("Enter your first name: ")

# Get user's last name
last_name = input("Enter your last name: ")

# Concatenate first and last name to get full name
full_name = first_name + " " + last_name

# Print personalized greeting
print("Hello, " + full_name + "! Welcome!")
