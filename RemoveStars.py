class RemoveStars:
    def removeStars(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == '*':
                if len(st)>0:
                    st.pop()
            else:
                st.append(ch)
        return "".join(list(st))