class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for paren in s:
            if paren in p_dict:
                stack.append(paren)
            else:
                if not stack or paren != p_dict[stack.pop()]:
                    return False

        return True if not stack else False

# string solution is a bit slower but more readable
#        n = -1
#        while n != len(s):
#            n = len(s)
#            s = s.replace("()", "")
#            s = s.replace("[]", "")
#            s = s.replace("{}", "")
        
#        if len(s) == 0:
#            return True
#        return False
