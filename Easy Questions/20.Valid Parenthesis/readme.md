# Valid Parentheses Problem

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples
- Input: `s = "()"`  
  Output: `true`
- Input: `s = "()[]{}"`  
  Output: `true`
- Input: `s = "(]"`  
  Output: `false`

## Approach
To determine if the string is valid, we can use a stack data structure:
1. Use a dictionary to map closing brackets to their corresponding opening brackets.
2. Iterate through each character in the string:
   - If the character is a closing bracket, check if it matches the most recent unmatched opening bracket (top of the stack).
   - If it does not match, the string is invalid.
   - If it matches, pop the top of the stack.
   - If the character is an opening bracket, push it onto the stack.
3. After processing all characters, if the stack is empty, all brackets matched correctly; otherwise, the string is invalid.

## Complexity Analysis
# Time Complexity: O(n), where n is the length of the input string.
Each character is processed once, and stack operations (push and pop) are O(1).
# Space Complexity: O(n), where n is the length of the input string.
In the worst case, all characters are opening brackets and are pushed onto the stack.
## Explanation
- Bracket Map: A dictionary bracket_map is used to store the corresponding opening brackets for each type of closing bracket.
- Stack: A list stack is used to keep track of the opening brackets encountered in the string.
- Iteration: The code iterates over each character in the string:
If the character is a closing bracket (exists in bracket_map), it checks whether the stack is non-empty and if the top element of the stack matches the corresponding opening bracket from bracket_map. If not, it returns False.
If the character is an opening bracket, it pushes it onto the stack.
- Final Check: After processing all characters, it checks if the stack is empty. If it is empty, all brackets were matched correctly; otherwise, the string is invalid.
