# Name: Alberto 
# Date:February 5, 2023

# Program 1: Output's Hello World!
print("\n\nProgram 1")
print(" Hello World!")

# Program 2: Ask user for input(name), greets the user with a message.
print("\n\nProgram 2")
name = input("What is your name? ")
print(("Nice to meet you!"), name)

# Program 3: Modification of Program 2
print("\n\nProgram 3")
name = input("What is your name? ")
if name == 'Angel' or name == 'Zoe':
    print("Nice to meet you!", name)
else:
    print("Invalid User")

# Program 4 : Computes area of a circle
print("\n\nProgram 4")
r = float(input("Enter radius value: "))
p = 3.14159

A = p * r ** 2
print("The area of the circle is: ", A)

# Program 5: Compute MPG for a car
print("\n\nProgram 5")
m = float(input("How many miles have you driven? "))
g = float(input("How many gallons have you used"))

mpg = m / g 
print("The total mpg your vehicle use is: ", mpg)

# Program 6: Converts degreees Fahrenheit to degrees Celsius
print("\n\nProgram 6")
# Celsius = (Fahrenheit - 32)* 5 / 9
F = float(input("What is the current degrees in Fahrenheit? "))
Celsius_= (F - 32) * 5 /9
print("The current degrees in Celsius is: ", Celsius_)

# Program 7:
print("\n\nProgram 7")
Depart = int(input("When will you depart? "))
Legnth_of_Stay = int(input("How long will you stay "))
Total = Depart + Legnth_of_Stay

Final = Total % 7
print("You will be arrving back on: ", Final)