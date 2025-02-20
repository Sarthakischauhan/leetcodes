class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        } 
        if not digits: return []
        result = []

        def backtrack(digit, letters):
            nonlocal result

            if not digit:
                result.append(letters)
                return 

            for letter in keyboard[digit[0]]:

                letters += letter
                backtrack(digit[1:], letters) 
                # Set letters back to what they were
                letters = letters[:-1]
                
        backtrack(digits, "")
        return result

        
