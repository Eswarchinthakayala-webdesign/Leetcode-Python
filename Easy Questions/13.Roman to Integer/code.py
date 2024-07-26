def romanToInt( s):
        romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num,prev_num=0,0
        for char in s:
            value=romans[char]
            if prev_num<value:
                num+=value-2*prev_num
            else:
                num+=value
            prev_num=value
        return num
            
