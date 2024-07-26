def longestCommonPrefix(strs):
     if not strs:
          return ""

     strs.sort()
     print(strs)
     first=strs[0]
     last=strs[-1]
     i=0

     while i<len(first) and i<len(last) and first[i]==last[i]:
          print(first[i], last[i])
          i+=1
     return first[:i]


strs=["ramu","famu","kamu"]
print(longestCommonPrefix(strs))
