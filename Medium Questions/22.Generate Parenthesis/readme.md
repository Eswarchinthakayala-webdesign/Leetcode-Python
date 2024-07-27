# Generate Parentheses

## Problem Description
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Examples

#### Example 1
- **Input:** `n = 3`
- **Output:** `["((()))","(()())","(())()","()(())","()()()"]`

#### Example 2
- **Input:** `n = 1`
- **Output:** `["()"]`

## Approach
To generate all combinations of well-formed parentheses for a given number of pairs `n`, we use a backtracking approach. The idea is to add '(' and ')' characters while maintaining the balance of the parentheses. Specifically:
1. We only add '(' if we still have some left to add.
2. We only add ')' if the number of ')' characters does not exceed the number of '(' characters at any point.

## Explanation
Main Function: generateParenthesis(n)
## Initialization:

result = []: This initializes an empty list result to store all valid combinations of parentheses.
Backtrack Function Call:

backtrack("", 0, 0): This calls the helper function backtrack with the initial parameters:
s = "": An empty string to build the combination.
left = 0: Counter for the number of '(' added.
right = 0: Counter for the number of ')' added.
Return Result:

return result: After the backtracking process is complete, it returns the result list containing all valid combinations.
Helper Function: backtrack(s, left, right)
This function uses recursion to build the combinations of well-formed parentheses.

# Base Case:

- if len(s) == 2 * n: If the length of the current string s is equal to 2 * n (indicating that we have used all n pairs of parentheses):
result.append(s): Add the current combination s to the result list.
return: Exit the function to backtrack.
Adding '(':

- if left < n: If the number of left parentheses left is less than n:
backtrack(s + '(', left + 1, right): Add a '(' to the string s, increment the left counter, and make a recursive call to continue building the string.
Adding ')':

- if right < left: If the number of right parentheses right is less than the number of left parentheses left (to ensure valid pairing):
backtrack(s + ')', left, right + 1): Add a ')' to the string s, increment the right counter, and make a recursive call to continue building the string.
