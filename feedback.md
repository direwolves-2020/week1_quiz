# Palindrome

I think you have the right basic idea in that you're iterating through the input string and checking for a palidrome at each character point. This and the logic you've used is further clarified by the numerous comments that you've added to your code. So in effect you've broken the main problem down into a few parts

 1. Iterating through the string
 2. Checking for a palindrome
 3. Checking for the max length palindrome.

That being the case, I would have had a separate private function that would do the job of checking for a palindrome. This function would take in the main string and perhaps an index that represented the mid-point (or the starting point from which to check left and right for the palindrome criteria) and would return the substring that it saw was a palindrome for that given index. This function would be called in each iteration your outer for loop.

For the core palindrome checking logic, you don't really need the potential_palindrome check. A string of one character is a palindrome so you could have the private function keep a default return value as the character at the index that its called with. Then your potential_palindrome check logic would not be needed since it would just flow in with the rest of the logic to detect any longer palindrome.

Given that you just need to return the max-length palindrome substring, I wouldn't bother keeping a list of palindromes. Instead I would store the return variable of the palindrome function in a variable if, and only if, the value returned was longer than the one returned from the call in the previous iteration. That way we only store the one value that will be the max at the end of the outer for loop.

Also, I would have assert statements at the end of my code rather than a print(), to prove that this code works for a few other inputs.

Finally, I would've gotten rid of the spurious commented code before submitting it. 


# Binary
Good amount of comments in the code

In the decimal_to_binary, I would take care of all of the edge cases up front prior to body of the loop. i.e. the check for `input_number == 0`. 

In terms of the actual looping logic, you shouldn't need the nested loop, instead you should be able to accomplish what you need with a single loop. Also, in general, a loop that counts down it not a problem, but it's more readable to have a loop with a counter that counts up (increments) rather than a decrementing one: Just is a little more intuitive to read.

```
for i in range(0, length_of_list):
    decimal_value = binary_as_list.pop() * 2**i
```

Missing assert statements, but by and large this is ok.
