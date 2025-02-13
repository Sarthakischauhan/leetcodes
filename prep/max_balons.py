class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {b:0 for b in "balon" }

        for t in text:
            if t in "balloon":
                letters[t] = letters.get(t, 0) + 1
        
        # Set of conditions to make it work
        # if letters["l"] != letters["o"]: return 0 
        if not all(letters.values()): return 0

        return min(letters["b"], letters["a"], letters["n"], letters["l"] // 2, letters["o"] // 2)
 

        
