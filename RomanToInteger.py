'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
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
    
