class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        result = ""
        if (strs == [""] or strs == []):
            return result
        
        while (idx < len(strs[0])):
            temp = strs[0][idx]
            for i in range(1, len(strs)):
                if (idx == len(strs[i]) or temp != strs[i][idx]):
                    return result
            result += temp
            idx += 1 
                                             
        return result
