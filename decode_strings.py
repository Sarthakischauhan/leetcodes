class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):               
            if s[i] != "]":
                stack.append(s[i])
            else:
                newstr = ''
                while stack[-1] != "[":
                    newstr = stack.pop() + newstr
                    print(newstr)
                stack.pop()
                mul = ''
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul
                stack.append(int(mul) * newstr)
        return ''.join(stack)

# O(n),Time complexity, mostly solved using Neetcode's approach.
# O(n), space complexity.

