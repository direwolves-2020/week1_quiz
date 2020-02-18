def to_binary(num):
    #using recursion to convert decimal to binary
    if num > 1: 
        #using floor division for next division round accuracy 
        to_binary(num // 2)
    print(num % 2, end= '')

def to_decimal(bin):
    #creating variables to help with calculations in the while loop
    bin1 = bin
    decimal = 0
    i = 0
    n = 0
    while(bin != 0):
    #taking modulo of binary
        dec = bin % 10
    #adding the remainder to decimal after 
    #multiplying by two to the power of the position of i
        decimal = decimal + dec * pow(2, i)
    #updating binary by dividing by 10 and rounding down for even division
        bin = bin//10
    #continue iterating until complete
        i += 1
    print(decimal)

to_decimal(100)
to_decimal(101)
to_decimal(1001)

to_binary(8976)