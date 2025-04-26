"""
https://algo.itcharge.cn/Solutions/0300-0399/decode-string

important to understand the generalized form of a expression:
    expression = string + number * [ expression ] 
here string can be "" and number can be 0. 
That will lead to a more concise solution
"""

from collections import deque 

class Solution(object):
    def decodeString(self, s):
        stack = deque()
        for ch in s:
            if ch.isdigit(): 
                stack.append(ch)
                print("1# ", stack)
            elif ch == '[':
                number = ''
                while(stack):
                    x = stack.pop()
                    if (not isinstance(x, str) or not x.isdigit()): 
                        stack.append(x)
                        break
                    number = x + number
                stack.append(int(number))
                print("2# ", stack)
            elif ch == ']':
                string = ''
                x = stack.pop()
                while(isinstance(x, str) and stack):
                    string = x + string
                    x = stack.pop()
                rep = x
                string = string * rep
                stack.append(string)
                print("3# ", stack)
            else:
                stack.append(ch)
                print("4# ", stack)
        print(stack) 
        # combine the strings 
        ret = ""
        while stack:
            ret = stack.pop() + ret
        
        return ret



s = Solution()
# s.decodeString("12[ab]")
s.decodeString("3[a]2[bc]")
#s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")