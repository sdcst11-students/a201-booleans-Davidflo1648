#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

def check_integer(number):
    if isinstance(number, int):
        print("The number is an integer")
    else:
        print("The number is not an integer")
