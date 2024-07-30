def trailing_zeroes(n):
    count,power=0,5
    while n>=power:
        count+=n//power
        power*=5
    return count

print(trailing_zeroes(3))

print(trailing_zeroes(5))
