def reverse(x):
    max=2**31-1
    min=-2**31
    sign=-1 if x<0 else 1
    x=abs(x)
    reversed_num=0
    while x!=0:
        r=x%10
        x//=10
        if reversed_num>(max-r)//10:
            return 0
        reversed_num=reversed_num*10+r
    return reversed_num
x=-2147483648
print(reverse(x))
