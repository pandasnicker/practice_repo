def isValid(s):
        if len(s) == 0:
            return True
    
        if len(s) == 1:
            return False
        
        lst = []
        
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                lst.append(s[i])
            
            elif s[i] in [')', ']', '}'] and len(lst) > 0:
                x = lst.pop()
                if (x == '(' and s[i] == ')') or (x == '[' and s[i] == ']') or (x == '{' and s[i] == '}'):
                    continue
                else:
                    return False
            else:
                return False

        return not len(lst)

print(isValid('{}}'))
