class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1] 
                if (diff < 0):
                    stack.pop()
                elif diff == 0:
                    stack.pop() 
                    ast = 0
                else:
                    ast = 0
            if ast:
                stack.append(ast)
        return stack

# terrible question, I solved it for one pass but had to look at neetocde.io for further question breakadown. 
# O(n) time complexity 
# O(n) space complexity. 
