def maxArea(height):
   max_area,left,right=0,0,len(height)-1
   while left<right:
       area=min(height[left],height[right])*(right-left)
       max_area=max(area,max_area)
       if height[left]<height[right]:
           left+=1
       else:
           right-=1
   return max_area

height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))
