class MaximumNumberOfVowels:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        vowelCount = maxVowelCount = sum([1 if ch in vowels else 0 for ch in s[:k]])
        for i in range(len(s)-k):
            vowelCount += (s[i+k] in vowels) - (s[i] in vowels)
            if vowelCount>maxVowelCount: maxVowelCount = vowelCount
        return maxVowelCount