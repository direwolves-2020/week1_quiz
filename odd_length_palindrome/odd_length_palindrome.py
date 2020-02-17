# Week 1 quiz

def is_palindrome(my_str):
"""
Generic palindrome function to determine if a string is a palindrome
"""
    if(my_str[::-1]) == my_str:
        return True
    else:
        return False


def palindrome(my_string):
""" 
Write a function that takes in a string and returns the longest odd length palindrome. (For example if the input string was 'abcracecarxyz' the solution would be 'racecar').
If you would like you can consider even length palindromes along with odd length palindromes.
"""
    
    my_list = []
    length = 0
    final_list = []
    longest = 0

    #get list of all substrings in the main string
    for i in range(0, len(my_string)):
        for j in range(i, len(my_string)):
            if my_string[i:j+1] not in my_list:
                my_list.append(my_string[i:j+1])
            

    #determine if any of the substrings are themselves palindromes
    #if they are, count the length of the string 
    #use modulus to determine even or odd
    for s in my_list:
        result = is_palindrome(s)
        length = len(s)
        odd_even = length % 2

        #if palindrome and odd, add to new list and 
        if result == True and odd_even == 1:
            final_list.append(s)
            #longest = max(len(i) for i in final_list)
            longest = max(final_list, key = len)

    return longest

assert palindrome("abcracecarxyz") == "racecar"
