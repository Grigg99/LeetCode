class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        max_length = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        counter = 0
        for i in range(k):
            if s[i] in vowels:
                counter += 1
        max = counter
            
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                counter -= 1
            if s[i] in vowels:
                counter += 1
            
            if max < counter:
                max = counter
            
        return max