def removedup(nums):
    nums[:]=sorted(set(nums))
    return len(nums)

nums=[1,1,3]
print(removedup(nums))
