def majority(nums):
    maj_element,count=None,0
    for num in nums:
        if count==0:
            maj_element=num
        if   num==maj_element:
            count+=1
        else:
            count-=1
    return maj_element

nums=[2,2,1,1,1,2,2]
print(majority(nums))
