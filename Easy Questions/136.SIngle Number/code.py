def singleNumber(nums):
    output=0
    for num in nums:
        output=output^num
    return output


nums=[1]
print(singleNumber(nums))
