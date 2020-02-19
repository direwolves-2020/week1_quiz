# Week 1 quiz

def decimal_to_binary(num):
    """
    This function returns the decimal value of a binary input
    """

    #binary = bin(num).replace("0b", "")

    quotient = 0
    binary = ''

    #divide the number by 2
    #the remainder becomes the bit
    #the number becomes the quotient
    #combine all the bit to get the full binary number
    while num > 0:
        quotient = int(num / 2)
        remainder = num % 2
        num = quotient
        binary += str(remainder)

    binary = binary[::-1]

    return int(binary)

assert decimal_to_binary(9) == 1001
assert decimal_to_binary(14) == 1110
