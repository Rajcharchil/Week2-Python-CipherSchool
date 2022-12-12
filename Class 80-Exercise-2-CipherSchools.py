# Exercise
# Define is_palindrom funtion that take one word in string as input
# and return True if it is palindrom else return false

def is_palindrom(word):
    reversed_word= word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

def is_palindrom(word):

    if word == word[::-1]:
        return True

    return False

def is_palindrom(word):
    return word == word[::-1]
a=input("Enter the word here::")
print(is_palindrom(a))
b=input("Enter the word here::")
print(is_palindrom(b))