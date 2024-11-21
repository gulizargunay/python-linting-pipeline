from typing import List, TypeVar, Union, Any, Protocol

def reverse_string(s: str) -> str:
    """
    Returns the string in the reverse order

    Parameters:
    (s: str) : The string to reverse
    str : the reversed string.
    """
    return s[::-1]





def count_vowels(s: str) -> int:

    """
    Counts the the number of vowels in the given string.

    Parameters:
    (s: str) : The string to count vowels.
    int : the number of vowels in the given string.

    """

    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)




def is_palindrome(s: str) -> bool:

    """
    Checks if the given string is a palindrome.

    Parameters:
    (s: str) : The string to check.
    bool : true if the given string is a palindrome, otherwise false.
    """

    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]



def find_longest_word(sentence: str) -> str:

    """
    Find the longest word in the given sentence.

    Parameters:
    (sentence: str) : The given sentence.
    str : the longest word in the sentence, or an empty string if no words.

    """

    words = sentence.split()
    return max(words, key=len) if words else ''

def test():
    print("Hello, World")

def bad_code():
    x=5
    print("The value of x is {5}")
