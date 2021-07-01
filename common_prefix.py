
def longestCommonPrefix(strs):
        if len(strs) == 0:
            return ""
        
        min_len = min(len(_) for _ in strs)
        
        pref = strs[0][:min_len]

        for _ in strs:
            i = min_len
            while i > 0:
                if pref[:i] != _[:i]:
                    i -= 1
                    pref = pref[:i]
                else:
                    break
                    
        return pref



print(longestCommonPrefix(['Gulam','Gulab']))