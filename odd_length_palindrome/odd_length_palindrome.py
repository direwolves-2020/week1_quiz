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
    s_length = 0
    final_list = []

    #get list of all substrings in the main string
    for i in range(0, len(my_string)):
        for j in range(i, len(my_string)):
            if my_string[i:j+1] not in my_list:
                my_list.append(my_string[i:j+1])
    
    #instead of nested loop use single loop
    #from each character get the longest palindrome by checking to the left and right (work outward to try each substring that you form)
    #use slicing [x-i:x+i:1]

    #determine if any of the substrings are themselves palindromes
    #if they are, count the length of the string 
    #use modulus to determine even or odd

    longest = 0
    longest_string = ''

    for s in my_list:
        result = is_palindrome(s)
        s_length = len(s)
        odd_even = s_length % 2

        #if palindrome and odd
        #dont need to create new list for the final result, can just check if s is longer than longest, otherwise s is longest
        if result == True and odd_even == 1:
            if(s_length) > longest:
                longest = s_length
                longest_string = s

            #if palindrome and odd, add to new list
            # if result == True and odd_even == 1:
            #     final_list.append(s)
            #     longest = max(final_list, key = len)
                
    return longest_string

assert palindrome("abcracecarxyz") == "racecar"
assert palindrome("kayak") == "kayak"