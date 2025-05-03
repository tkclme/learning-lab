def is_palindrome(word:str) -> bool:
    
    """ Renvoie si un mot est un palindrome """
    return True if word == word[::-1] else False


print(is_palindrome("politesse"))
print(is_palindrome("kayak"))