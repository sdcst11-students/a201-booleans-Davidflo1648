#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"


numb = input("Enter a number: ")

try:
    number = int(numb)
    print(f"{number} is an integer.")
except ValueError:
    print(f"{numb} is not an integer.")



