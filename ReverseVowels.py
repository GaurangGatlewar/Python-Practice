class ReverseVowels:
    def reverseVowels(self, s: str) -> str:
        temp = [x for x in s]
        start = 0
        end = len(s)-1
        while end>start:
            if temp[start].lower() not in ('a','e','i','o','u'):
                start += 1
            elif temp[end].lower() not in ('a','e','i','o','u'):
                end -= 1
            else:
                temp[start],temp[end] = temp[end],temp[start]
                start += 1
                end -= 1
        return "".join(temp)