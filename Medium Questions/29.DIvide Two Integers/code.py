def divide(dividend,divisor):
    MAX=2**31-1
    MIN=-2**31
    sign= -1 if(dividend * divisor)<0 else 1
    dividend=abs(dividend)
    divisor=abs(divisor)
    quotient=0
    while dividend>=divisor:
        count=0
        while dividend>=(divisor<<(count+1)):
            count+=1
        quotient+=1<<count
        dividend-=divisor<<count
    result=sign*quotient
    if result<MIN:
        return MIN
    elif result>MAX:
        return MAX
    else:
        return result



dividend=7
divisor=-3
print(divide(dividend,divisor))
