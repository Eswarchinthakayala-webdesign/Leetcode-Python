def lastword(s):
    s=s.split(" ")
    result=[]
    for word in s:
        if word!="":
            result.append(word)
    return len(result[-1])
s= "  fly me   to   the moon  "
print(lastword(s))
