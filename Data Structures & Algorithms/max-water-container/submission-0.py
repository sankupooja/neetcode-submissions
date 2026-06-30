class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        i,j=0,len(heights)-1

        while i<j:

            minimum=heights[i] if heights[i]<heights[j] else heights[j]
            value=(j-i)*minimum
            
            if max<value:
                max=value
            
            if heights[i]<heights[j]:
                i+=1
            else:
                j=j-1
        
        return max


        