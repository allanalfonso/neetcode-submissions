class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])
            elif not stack:    #if stack is empty, then no opening brackets
                return False
            elif s[i] == ")":
                if stack.pop() != "(":
                    return False
            elif s[i] == "}":
                if stack.pop() != "{":
                    return False
            elif s[i] == "]":
                if stack.pop() != "[":
                    return False

        if stack:           #if there are still items left in the stack, then there are no closing brackets
            return False
        else:
            return True


                    