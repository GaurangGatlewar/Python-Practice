class GreatestCommonDivisorOfStrings:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)*len(str2) == 0:
            return ""

        if str1 == str2:
            return str1

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        str3 = str1[:len(str1)-len(str2)]
        common = self.gcdOfStrings(str2, str3)
        if len(common) == 0:
            return ""
            
        str4 = common*(len(str1)//len(common))
        if str1 != str4:
            return ""
        else:
            return common