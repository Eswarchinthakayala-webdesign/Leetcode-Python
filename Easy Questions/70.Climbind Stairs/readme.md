# Climb Stairs Function

## Approach

1. **Initialize the Steps List**:
   - Start with a list `steps` containing the number of ways to climb 1, 2, and 3 steps: `[1, 2, 3]`.

2. **Handle Larger Values of n**:
   - If `n` is greater than 3, use a loop to calculate the number of ways to climb each additional step from 4 to `n`.
   - For each step `i` from 4 to `n`, append `steps[i-1] + steps[i-2]` to the `steps` list. This follows the Fibonacci sequence, where each step can be reached from the two previous steps.

3. **Return the Result**:
   - Return `steps[n-1]`, which contains the number of ways to climb `n` steps.

## Code Snippet

```python
def climbstairs(n):
    steps = [1, 2, 3]
    if n > 3:
        for i in range(3, n):
            steps.append(steps[i-1] + steps[i-2])
    return steps[n-1]

n = 4
print(climbstairs(n))  # Output: 5
```
**Time Complexity**
The time complexity is O(n), where n is the number of steps. This is because the function iterates from 3 to n to calculate the number of ways to climb each step.
**Space Complexity**
The space complexity is O(n) because the function uses a list steps to store the number of ways to climb each step up to n.
**Explanation**
Dynamic Programming: The function uses a dynamic programming approach to calculate the number of ways to climb n steps. By storing the results of previous calculations, it efficiently computes the result for larger values of n.
Base Cases: The initial values in the steps list ([1, 2, 3]) represent the number of ways to climb 1, 2, and 3 steps, respectively.
Iteration: For values of n greater than 3, the function iterates and calculates the number of ways to climb each step using the results of the previous two steps.
