def simplifypath(path):
    path=path.split("/")
    stack=[]
    for value in path:
        if value=="..":
            if stack:
                stack.pop()
        elif value=="." or value=="":
            continue
        else:
            stack.append(value)
    return "/"+"/".join(stack)

path="/home/"
print(simplifypath(path))
