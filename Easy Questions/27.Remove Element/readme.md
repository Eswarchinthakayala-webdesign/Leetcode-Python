## removeElement Function
# Description
The removeElement function removes all occurrences of a specified value val from an integer array nums in-place. The order of the elements may be changed. The function returns the number of elements that are not equal to val.
## Explanation
The function uses a two-pointer technique to efficiently remove all occurrences of val from nums:

Initialize a pointer k to 0. This pointer keeps track of the position where the next non-val element should be placed.
Iterate through each element in the array with a pointer i.
If nums[i] is not equal to val, place nums[i] at nums[k] and increment k.
After iterating through the array, k will be the number of elements that are not equal to val, and the first k elements of nums will be the elements that are not equal to val.
Constraints
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
Testing
The function can be tested using the following approach:

Create an input array nums and a value val.
Call removeElement(nums, val).
Verify that the function returns the correct count k.
Verify that the first k elements of nums are correct (they do not contain val).
## Time Complexity
The time complexity of the removeElement function is 𝑂(𝑛)
n is the length of the input array nums. This is because the function iterates through each element of the array exactly once.

The loop runs from 0 to n-1, which means it performs 
𝑛
n iterations.
Each iteration performs a constant amount of work, including checking if the current element is equal to val and, if not, placing it at the next position tracked by k.
Therefore, the overall time complexity is 𝑂(𝑛)
# Space Complexity
The space complexity of the removeElement function is O(1), meaning it uses a constant amount of extra space.

The function only uses a few additional variables (i and k) for the iteration and tracking the position of non-val elements.
No additional data structures are used that scale with the input size.
Therefore, the overall space complexity is O(1).
