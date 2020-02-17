# Week 1 quiz

def binary_to_decimal(num):
    """
    This function converts a binary number to its corresponding decimal number
    Iterate through the length of the binary number and based on the position, square the digit
    """

    #separate the number into digits
    digits = [int(x) for x in str(num)]
    decimal = 0

    #multiply each digit by the square of its position
    for i in range(len(digits)):
        decimal += (2**i) * digits[i]

    #can also just use the int function
    #decimal = int(str(num), 2)

    return decimal

assert binary_to_decimal(1001) == 9

