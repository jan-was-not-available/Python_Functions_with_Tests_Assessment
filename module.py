'''
Complete the two functions below to show what
you've learned about writing functions in Python.
All tests must pass to receive credit.
'''
'''sum_list'''
# sum_list takes a list of integers and returns the sum
# of all numbers in the list.
#
# Examples:
#   sum_list([1, 2, 3]) -> 6
#   sum_list([5]) -> 5
#   sum_list([]) -> 0
#
# Requirements:
#   - Must use iteration (a loop)
#   - Do NOT use the built-in sum() function
#   - Do NOT print anything
#
def sum_list(numbers: list) -> int:
    output = 0 
    idx = 0
    while idx < len(numbers):
        curr_num = numbers[idx]
        output += curr_num
        idx += 1
    
    return output
    
          
    return sum_list
    pass


'''count_letter'''
# count_letter takes two arguments:
# a string and a single character.
# It returns the number of times that character
# appears in the string.
#
# Examples:
#   count_letter("hello", "l") -> 2
#   count_letter("banana", "a") -> 3
#   count_letter("apple", "z") -> 0
#
# Requirements:
#   - Must use iteration (a loop)
#   - Must return an integer
#   - Do NOT use the built-in count() method
#   - Do NOT print anything
#
def count_letter(s: str, letter: str) -> int:
    count = 0 
    idx = 0
    while idx < len(s):
        curr_letter = s[idx]
        if curr_letter == letter:
            count += 1
        idx += 1
    return count
    pass




''' Extra Credit Challenge'''
''' is_palindrome '''
# is_palindrome takes a string and returns True if the string
# reads the same forwards and backwards. Otherwise return False.
#
# Examples:
#   is_palindrome("racecar") -> True
#   is_palindrome("level") -> True
#   is_palindrome("hello") -> False
#
# Requirements:
#   - Return a Boolean value
#   - Do NOT use the built-in reversed() function
#   - Do NOT print anything
#
def is_palindrome(s: str) -> bool:
    reverse_s = ""
    idx = len(s)-1

    while idx >= 0:
        char = s[idx]
        reverse_s = reverse_s + char
        idx -= 1
    
    # for char in s:
    #   reverse_s = char + reverse_s

    if reverse_s == s:
        return True
    else:
        return False
    pass