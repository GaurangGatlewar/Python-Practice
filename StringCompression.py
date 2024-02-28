class StringCompression:
    def compress(self, chars: List[str]) -> int:
        count = 1
        location = 0
        previous = chars[0]
        for i in range(1,len(chars)):
            if chars[i] == previous:
                count += 1
            else:
                chars[location]=previous
                location += 1
                if count != 1:
                    for ch in str(count):
                        chars[location]=ch
                        location += 1
                    previous = chars[i]
                    count = 1
                previous = chars[i]

        chars[location]=previous
        location += 1
        if count != 1:
            for ch in str(count):
                chars[location]=ch
                location += 1
            
        return location