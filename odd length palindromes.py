"""def palindrome(a_string):

    #Creating a function that reverses a string
    def string_reverser(string):
        #creating variable string length, which gives me the starting point...
        #..for reversing my string. also serves as a counter for while loop.
        string_length = len(string) - 1

        #initializing an empty string for the final value
        reverse_string = ""

        #now utilizing string_length to pull as a reference for each string element
        while string_length > -1:
            #appending the reverse-most value to the new reverse string
            reverse_string += string[string_length]
            #counting the counter down one
            string_length -= 1
        return(reverse_string)


    def string_splitter(string):
        left_side_string = ""
        right_side_string = ""
        list_of_palindromes=[]
        #I need this initial for loop because each element in the string needs the opportunity to be the central point
        for x in range(0,len(string)):
            #Accounting for edge cases
            if x == 0 or x == 1 or x == len(string) or x == len(string) - 1:
                pass
            else:
                index = string[x]
                print("The index is:", index)
                left_side_string = string[:x+1]
                right_side_string = string[x:]
                print("original left side ", left_side_string)
                print("original right side ", right_side_string)
                
                #Ok. so now that I have an iterator that makes left and right sides,
                #I need to make another for loop that iterates through the left/right sides
                size_of_smallest_string = min(len(left_side_string),len(right_side_string))
                for y in range(0, size_of_smallest_string):
                    left_side_string = left_side_string[:y]
                    right_side_string = string_reverser(right_side_string)
                    print("ADJUSTED left side string ",left_side_string)
                    print("ADJUSTED right side string ",string_reverser(right_side_string))
                        #print("PALINDROME")

                #for x in len(min(left_side_string,right_side_string))
    
    #I dont think I need any of that. I think that literally the only thing I need
    #is that bottom part that takes the index, adds one, makes a value (which needs to be reversed) , minuses one , and then compares the two values.
    
    #Above I actually made something that could be relatively close to the even-palindrome



    
    string_splitter(a_string)
"""





def palindrome(a_string):
    #Initializing this list because it needs to account for the fact that there may be more than one palindrome in the string 
    list_of_palindromes = []
    #The first for loop is allowing each element in the list to be the central point
    for x in range(0,len(a_string)):
        #Accounting for edge cases because you can't have a palindrome at the first or last element of the string
        if x == 0  or x == len(a_string):
            pass
        else:
            #initializing a palindrome variable that is used for the logic that follows
            #This variable returns a string that takes the index, goes up/down by one element and if those two variables are equal, we have a palindrome.
            #its called potential palindrome because the center changes with each iteration of the for loop, so this is the first test to see if we may have a palindrome
            potential_palindrome = a_string[x-1:x+2]
            #This logic triggers when we encounter a palindrome in the wild
            if potential_palindrome[0] == potential_palindrome[-1]:
                #I need to make a new variable that holds the final output because 'potential palindrome' variable changes with each iteration of the index
                real_palindrome = potential_palindrome
                #Incrementor for the while loop starts at two because we already know the first element above/below the center point match as we found in our potential palindrome
                incrementor = 2
                #The max incrementor variable is used in the while loop so that it can only go as long as the shortest side. otherwise, the output will get wonky
                max_incrementor = min(len(a_string[:x]), len(a_string[x+1:]))
                #This while loop increments out one from the center point as long as the new increments are equal to each other
                while real_palindrome[0] == real_palindrome[-1] and incrementor <= max_incrementor:                
                    real_palindrome = a_string[x-incrementor : x+incrementor+1]
                    incrementor +=1
                #The return statement needs to return the 1 to -1 elements because it currently only breaks when it sees that the next increment is no longer equal
                #unless... of course.... if its a perfect palindrome
                if real_palindrome[0] == real_palindrome[-1]:
                    list_of_palindromes.append(real_palindrome)
                else:
                    #If its not a perfect palindrome, then we need to remove those last two variables
                    list_of_palindromes.append(real_palindrome[1:-1])
    return max(list_of_palindromes, key=len)

#Its not super efficient because the while loop does an extra loop and i have to nest this extra if statement at the end
#also, the incrementor vairblae doesnt restart, which isn't actually a problem because that means that it'll only append palindromes that are larger than previous palindromes


print(palindrome('acaracecar'))

"""
def does_this_work(string):
    for x in range(0,len(string)):
        print(string[x-1:x+2])

does_this_work('racecarrz')"""