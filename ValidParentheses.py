class ValidParentheses():
    def __init__(self):
        self.par = {}
        self.par['('] = ')'
        self.par['{'] = '}'
        self.par['['] = ']'
        return

    def valid(self, word):
        l = []
        for c in word:
            if c in self.par.keys():
                l.insert(len(l),self.par[c])
            else:
                try:
                    temp = l.pop()
                    if(temp != c):
                        return (0)
                except:
                    return (0)

        if(len(l) == 0):
            return (1)
        else:
            return (0)

    def check(self):
        while(1):
            print ("Please enter string or type exit to terminate.")
            s = input()
            if(s == 'exit'):
                break
            if(self.valid(s) == 1):
                print ("The parentheses are valid")
            else:
                print ("The parentheses are invalid")
        return

if __name__ == '__main__':
    ValidParentheses().check()