def plusone(digits):
    sum=0
    re_sum=0
    result=[]
    for i in range(len(digits)):
        sum=sum*10+digits[i]
    sum=sum+1
    while sum!=0:
        r=sum%10
        sum//=10
        result.append(r)
    return result[::-1]





digits=[1,2,3]
print(plusone(digits))
