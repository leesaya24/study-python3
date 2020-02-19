class Solution:
    def romanToInt(self, s: str) -> int:
        idx = 0
        resultNum = 0
        while (idx < len(s)):
            
            if (s[idx:idx+1] == "I"):
                if (s[idx+1:idx+2] == "V"):
                    resultNum +=4
                    idx +=1
                elif(s[idx+1:idx+2] == "X"):
                    resultNum +=9
                    idx +=1
                else:
                    resultNum +=1
                    
            elif (s[idx:idx+1] == "X"):
                if (s[idx+1:idx+2] == "L"):
                    resultNum +=40
                    idx +=1
                elif(s[idx+1:idx+2] == "C"):
                    resultNum +=90
                    idx +=1
                else:
                    resultNum +=10
                   
                    
            elif (s[idx:idx+1] == "C"):
                if (s[idx+1:idx+2] == "D"):
                    resultNum +=400
                    idx +=1
                elif(s[idx+1:idx+2] == "M"):
                    resultNum +=900
                    idx +=1
                else:
                    resultNum +=100
                    
                    
            elif (s[idx:idx+1] == "V"):
                resultNum +=5
            elif (s[idx:idx+1] == "L"):
                resultNum +=50    
            elif (s[idx:idx+1] == "D"):
                resultNum +=500
            elif (s[idx:idx+1] == "M"):
                resultNum +=1000    
            
            idx +=1
        
        return resultNum
