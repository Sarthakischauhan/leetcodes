class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n = len(s)
        curr_sum = sum(c in vowels for c in s[:k])
        max_sum = curr_sum

        for i in range(k, n):
            curr_sum += int(s[i] in vowels) - int(s[i - k] in vowels)
            max_sum = max(max_sum, curr_sum)
        return max_su

# Kind of disappointed that I coulnd't solve it on my own
