class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        variable= -1
        if len(t)==0:
            return False
        for i in s:
            if variable == len(t)-1:
                return False

        
            for j in range(variable+1,len(t)):
                if i == t[j]:
                    
                        variable=j
                        break
                       
                    
                else:
                    if j== len(t)-1:
                        return False


        return True
        


        