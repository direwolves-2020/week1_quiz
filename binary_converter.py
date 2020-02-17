"""
write a method that takes binary numbers and outputs a base 10 number

Write a method that takes decimal numbers and returns it in binary notation
"""


def decimal_to_binary(decimal):
    number = int(decimal)

#Creating a function that takes the decimal number and converts it to a binary list
    def converting_the_number(num):
        decimal_number = num
        binary_list = []
        while decimal_number >= 1:
            if decimal_number % 2 == 0:
                binary_list.append('0')
            else: binary_list.append('1')
            decimal_number = int(decimal_number / 2)
        binary_list.reverse()
        final_output = ''.join(binary_list)
        return(final_output)
    
    print(converting_the_number(number))

#decimal_to_binary(156)
        
def binary_to_decimal(binary):
#converting to a string so that we can iterate through each digit in a for loop
    binary_number = str(binary)

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
binary_to_decimal(1100011)



