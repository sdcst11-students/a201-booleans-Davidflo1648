#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""

def check_password(sentence):
    if "password" in sentence:
        return "The sentence contains password"
    else:
        return "The sentence does not contain password"

user_input = input("Enter a sentence: ")
result = check_password(user_input)
print(result)
