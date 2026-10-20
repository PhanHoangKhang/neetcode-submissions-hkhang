class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for char in t:
            if char not in seen:
                return False
            else:
                if seen[char] == 0:
                    return False
                seen[char]-=1

        return True