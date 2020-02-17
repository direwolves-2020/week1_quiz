"""
write a method that takes binary numbers and outputs a base 10 number

Write a method that takes decimal numbers and returns it in binary notation
"""


def decimal_to_binary():
    #User input for the function
    input_number = input("What is the decimal number you would like to convert?\n> ")
    #this is the value that will be adjusted in the while loop below. I need to make a seperate value because incase someone tries to convert a 0, it should return a 0
    number = int(input_number)
    #Initilizaing the final output variable up here so that I can return a 
    final_output = 0

     #Initializing a list for the while loop to append to
    binary_list = []
    #This whole loop will run as long as the number is greater than or equal to 1
    while number >= 1:
        #If the number is even....
        if number % 2 == 0:
            #give it a '0'
            binary_list.append('0')
            #otherwise, it should be a 1
        else: binary_list.append('1')
        #then, according to the formula, we divide by 2, usint int to ensure no decimals carry
        #this also updates the decimal number variable so we can keep using the while loop
        number = int(number / 2)
    #once the while loop is finished, we have all the binary digits, but they need to be reversed    
    binary_list.reverse()
    #now transforming the list of binary digits into one number
    final_output = ''.join(binary_list)
    if input_number == 0:
        print(input_number)
        return input_number
    print(final_output)
    return(final_output)    

        
def binary_to_decimal():
    binary_number = input("What is the binary number you would like to convert?\n> ")

#converting to a string so that we can iterate through each digit in a list comprehension
    binary_number = str(binary_number)

#this bit of code turns the string of binary numbers into a list of seperate ints to iterate through
    binary_to_list = [int(x) for x in binary_number]
#making this binary_len variable which raises the binary_len to the 1 or 0 that coincides with the calculation
    binary_len = len(binary_number) - 1
#initializing the final_decimal value which will store the final output of the mathematical conversion
    final_decimal = 0
#looping through each 1/0 and raising it to the power of the nth digit
#The while loop starts at the first digit of the binary number and works toward the final digit
    while binary_len >-1:
        for x in binary_to_list:
            final_decimal += x * (2**(binary_len))
            binary_len -= 1
    print(final_decimal)
    return final_decimal

#This is the engine
def converter():
    print("Do you want to convert a decimal number to binary, or a binary number to decimal?")
    print("Type d2b for decimal to binary, otherwise type b2d for binary to decimal")
    response = input("> ")
    if response == "d2b":
        decimal_to_binary()
    elif response == "b2d":
        binary_to_decimal()
    else: 
        print("Oh- you're one of those people who don't listen to directions. cool.")

converter()


