class MergeStringsAlternately:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2

        if len(word2) == 0:
            return word1

        minLength = min(len(word1), len(word2))
        answer = ""
        for i in range(minLength):
            answer += word1[i] + word2[i]
        answer += word1[minLength:] + word2[minLength:]
        return answer