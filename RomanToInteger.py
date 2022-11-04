'''
my own submission to the Roman to Integer problem
'''
class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        intValue = 0
        
        validRomain = True
        skipNext = False
        
        s = s.upper()
        
        symbols= {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        if (len(s)>=1) and (len(s)<=15):            
            for i in range(len(s)):
                if s[i] not in symbols.keys():
                    validRomain = False            
        else:
            validRomain = False
        
        if validRomain:
            for i in range(len(s)):
                if skipNext:
                    skipNext = False
                    continue
                if i< (len(s)-1) :
                    if s[i] == 'I':
                        if s[i+1] == 'V':
                            intValue = intValue + 4
                            skipNext = True
                        elif s[i+1] == 'X':
                            intValue = intValue + 9
                            skipNext = True
                        else:
                            intValue = intValue + symbols[s[i]]
                    
                    elif s[i] == 'X':
                        if s[i+1] == 'L':
                            intValue = intValue + 40
                            skipNext = True
                        elif s[i+1] == 'C':
                            intValue = intValue + 90
                            skipNext = True
                        else:
                            intValue = intValue + symbols[s[i]]
                            
                    elif s[i] == 'C':
                        if s[i+1] == 'D':
                            intValue = intValue + 400
                            skipNext = True
                        elif s[i+1] == 'M':
                            intValue = intValue + 900
                            skipNext = True
                        else:
                            intValue = intValue + symbols[s[i]]
                    else:
                        intValue = intValue + symbols[s[i]]  
                else:
                    intValue = intValue + symbols[s[i]]
            
            return intValue
        else: 
            return -1
    
