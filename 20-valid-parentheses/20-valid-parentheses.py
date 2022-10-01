class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")":"(","]":"[", "}":"{"}
        for char in s:
            if char in dict:
                top = stack.pop() if stack else 'dummy'
                if dict[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack