def twoSum(nums,target):
    num_to_index={}
    for i,x in enumerate(nums):
        y=target-x
        if y in num_to_index:
            return [num_to_index[y],i]
        num_to_index[x]=i
    return []

nums=[2,7,11,15]
target=9
print(twoSum(nums,target))
