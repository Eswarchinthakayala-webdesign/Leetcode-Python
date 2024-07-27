## strStr Function
# Description
The strStr function finds the index of the first occurrence of the substring needle in the string haystack. If needle is not part of haystack, the function returns -1.
## Explanation
The function uses a sliding window approach to find the first occurrence of needle in haystack:

# Edge Case Handling:

If needle is an empty string, return 0 (although the problem constraints imply needle is never empty).
Iterate through haystack:

Use a loop to check each possible starting position in haystack where needle could fit.
For each starting position, check if the substring of haystack from that position matches needle.
Return the Starting Index:

If a match is found, return the starting index.
If no match is found after checking all positions, return -1
## Complexity Analysis
# Time Complexity
The time complexity of the strStr function is 
O((n−m+1)×m), where 
n is the length of haystack and 
m is the length of needle.
In the worst case, each of the 
n−m+1 starting positions is checked, and each check involves comparing up to m characters.
# Space Complexity
The space complexity is O(1) because no additional space is used that scales with the input size. Only a few extra variables are used for indexing and storing lengths.
