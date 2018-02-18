def main():
    file = open('input.txt','r+')
    full = file.read()
    file.close()
    lines = full.split('\n')
    t = int(lines[1].strip())
    A = ""
    for i in range(t):
        n,k,b = list(map(int,lines[i+2].strip().split(" ")))
        l = find(n,k,b)
        try:
            answer = ""
            for i in range(len(l)):
                answer += str(l[i]) + " "
            A += (answer.strip() + '\n')
        except:
            A += str(l) + '\n'
    
    fh = open('output.txt','w+')
    fh.write("The output is:\n")
    fh.write(A)
    fh.close()
    return

def find(n,k,b):
    if(b == 1):
        if(n<=k):
            return (n)
        else:
            return (-1)
    minsum = (b*(b+1))/2
    maxsum = minsum + (b*(k-b))
    if(n<minsum or n>maxsum):
        return (-1)
    
    answer = []
    minsum = (b*(b+1))//2
    start = int((n-minsum)//b)
    remainder = n - minsum - (b*start)
    if(remainder==0):
        for i in range(1,b+1):
            answer.append(start+i)
        return (answer)
    
    diff = k - (start+b)
    m = int(remainder//diff)
    spec = remainder - (diff*m)
    
    for i in range(1,b-m):
        answer.append(int(start+i))
        n -= int(start+i)
    
    for i in range(m):
        answer.append(int(k - i))
        n -= int(k - i)
        
    answer.append(n)
    
    return (answer)

main()