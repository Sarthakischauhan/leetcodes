class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        i = 0
        while ( i < len(chars)):
            char = chars[i]
            value = 0
            add = ""
            while ( i < len(chars) and chars[i] == char):
                value += 1
                i += 1
                if (value > 1):
                    str_value = str(value)
                    add = char + str_value
                else:
                    add += char
            chars[res:res+len(add)] = add
            res += len(add)
        return res

# Time complexity --> O(n)
# Space complexity --> O(n) but constant extra space
