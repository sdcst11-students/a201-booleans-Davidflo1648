#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math

a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))

def classify_triangle(a, b, c):
    # Calculate the squares of side lengths
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2
    
    # Check for right-angled triangle
    if a_squared + b_squared == c_squared or \
       b_squared + c_squared == a_squared or \
       c_squared + a_squared == b_squared:
        return "a right triangle"
    
    
    elif a_squared + b_squared > c_squared and \
         b_squared + c_squared > a_squared and \
         c_squared + a_squared > b_squared:
        return "an acute triangle"
    
    # Otherwise, it's an obtuse-angled triangle
    else:
        return "an obtuse triangle"

# Classify the triangle
result = classify_triangle(a, b, c)
print(f"That is {result}")