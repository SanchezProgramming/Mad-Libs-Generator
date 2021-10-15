"""
Story Example:

Hello, my name is _____ and my favorite color is _____.

My favorite animal is _____.

My favorite food is _____.
"""

# Give the user instructions
print("\nEnter the following:\n")
input1 = input("Name: ")        # Enter name
input2 = input("Color: ")       # Enter color
input3 = input("Animal: ")      # Enter favorite animal
input4 = input("Food: ")        # Enter favorite food

# Display the 1st sentence
print("\nHello, my name is " + input1 +
      " and my favorite color is " + input2 + ".")

# Display the 2nd sentence
print("My favorite animal is a " + input3 + ".")

# Display the 3rd sentence
print("My favorite food is a " + input4 + ".")