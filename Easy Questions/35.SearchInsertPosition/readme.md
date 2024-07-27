# searchInsert Function
## Description
The searchInsert function determines the index at which a target value should be inserted into a sorted array nums to maintain its sorted order. If the target value is already present in the array, the function returns the index of its first occurrence. If the target value is not present, it inserts the target into the array and then returns the index of the newly inserted value.
# Approach and Explanation
Check if Target is in Array:

If the target is not in nums, append target to nums.
This step ensures that we handle both the cases where target is already in the array and where it needs to be inserted.
Sort the Array:

Sort nums to maintain the sorted order after potentially appending the target.
Find and Return Index:

Iterate through the sorted array to find the index of the target and return it.
## Time Complexity: 
O(nlogn)
## Space Complexity: 
O(1)
