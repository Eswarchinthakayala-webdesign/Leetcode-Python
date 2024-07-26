def isPalindrome( x):
        temp=x
        if temp>0:
            rev_num=0
            while temp!=0:
                r=temp%10
                temp//=10
                rev_num=rev_num*10+r
            if(rev_num==x):
                return True 
        elif(x==0):
            return True           
        else:
            return False
            
