### Palindrome Integer Checker
 # Problem Description
The task is to determine if a given integer x is a palindrome. An integer is considered a palindrome if it reads the same backward as forward.
## Approach
# Handle Edge Cases:

Negative numbers are not palindromes due to the negative sign.
Numbers that end with zero are not palindromes (except zero itself).
## Reverse the Second Half of the Number:

Use mathematical operations to reverse the digits of the second half of the integer.
Compare this reversed half with the first half to check if the number is a palindrome.
## Explanation
Negative Numbers and Trailing Zeros:

Negative integers and integers ending with zero (except zero itself) cannot be palindromes due to their format.
Reversing Digits:

The code reverses the digits of the second half of the integer by extracting digits one at a time and building the reversed number.
Comparison:

After reversing half of the digits, compare the reversed half with the remaining first half of the number.
For numbers with an odd number of digits, dividing the reversed half by 10 removes the middle digit, which is not significant in palindrome checking.
Complexity Analysis
# Time Complexity:

The while loop runs approximately half the number of digits in x. This makes the time complexity O(log(n)), where n is the number.
# Space Complexity:

The solution uses a constant amount of extra space for variables (reversed_half and x).
Space Complexity: O(1)
