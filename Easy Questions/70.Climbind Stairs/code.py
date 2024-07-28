def climbstairs(n):
    steps=[1,2,3]
    if n>3:
        for i in range(3,n):
            steps.append(steps[i-1]+steps[i-2])
    return steps[n-1]


n=4
print(climbstairs(n))
