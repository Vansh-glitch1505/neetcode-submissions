class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {")": "(", "}": "{", "]": "["}

        for op in s:
            if op in closed:
                if stack and stack[-1] == closed[op]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(op)
        
        return stack == []  # True only if all brackets were matched