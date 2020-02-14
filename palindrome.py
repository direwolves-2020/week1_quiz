#This function prints longest palindrome substring of str[]
def longps(string): 
    #setting value for current highest length
    maxlen = 1
    start = 0
    #determining length of string for looping
    ran = len(string)
    #these values will be used to determine center points, low and high
    l = 0
    h = 0

    #considering each character as a center point
    for i in range(1, ran):
        #This will find the longest even lenght pal
        # we need to find the low center point and the high then expand outwards
        l = i-1
        h = i
        #once we have values to test for center we run this
        while l >= 0 and h < ran and string[l] == string[h]:
            #if high - low point plus 1 is greater than maxlen(originally 1) then start is defined as the low point
            if h - l + 1 > maxlen:
                start = l
                #maxlen would then be recalculated until eventually center point is found
                maxlen = h - l + 1
            #at this point you increment the l and h values to start pushing outwards evaluating if palidrome is still true
            l -= 1
            h += 1

        #This will find the longest odd pal
        #notice difference in h point is now i + 1 
        l = i-1
        h = i + 1
        #same while loop as above
        while l >= 0 and h < ran and string[l] == string[h]:
            if h - l + 1 > maxlen:
                start = l
                maxlen = h - l + 1
            l -= 1
            h += 1
        #printing the sliced list from the low point to the lowpoint plus the new maxlen
    print(" The longest palindrome substring is: " + string[start:start + maxlen])
    
longps("abcracecarxyz")
