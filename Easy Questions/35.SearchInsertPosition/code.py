def searchInsert(nums,target):
    if target not in nums:
        nums.append(target)
    nums.sort()
    for i in range(len(nums)):
        if nums[i]==target:
            return i


nums=[1,3,5,6]
target=2
print(searchInsert(nums,target))
