class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        valid_chars=[char.lower() for char in s if char.isalnum()]
        s="".join(valid_chars)
        l,r=0,len(s)-1
         
        while l<r:

            if s[l]==s[r]:
                r=r-1
                l=l+1
            else:
                return False
        return True