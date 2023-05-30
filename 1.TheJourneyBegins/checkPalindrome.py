# Given the string, check if it is a palindrome.

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

print(is_palindrome("aabaa")) # True