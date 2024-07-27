# Last Word Length Function

## Approach

1. **Split the String**:
   - Split the input string `s` by spaces to create a list of words. This may include empty strings where there were multiple spaces.

2. **Filter Out Empty Strings**:
   - Iterate through the list of words and filter out the empty strings to get a list of actual words.

3. **Return the Length of the Last Word**:
   - Return the length of the last word in the filtered list.

## Complexities

### Time Complexity
- The time complexity is \(O(n)\), where \(n\) is the length of the input string. This is because splitting the string and filtering out empty strings both take linear time.

### Space Complexity
- The space complexity is \(O(n)\) as well, where \(n\) is the length of the input string. This is due to storing the list of words after splitting the input string.


