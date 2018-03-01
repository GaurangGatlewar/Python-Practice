def main():
    la = 0
    print ("Enter the number of empty sequences and number of queries(Space separated)")
    try:
        N, Q = list(map(int, input().strip().split()))
    except:
        print ("Incorrect input format")
        return
    seq = []
    for i in range(N):
        ts = []
        seq.append(ts)
    for i in range(Q):
        print ("Enter the condition, x and y values(Space separated")
        try:
            cond, x, y = list(map(int,input().strip().split()))
        except:
            print("Incorrect input format")
            return
        index = ((x^la)%N)
        if(cond==1):
            seq[index].append(y)
        else:
            la = seq[index][y%len(seq[index])]
            print("The last answer is " + str(la))
    return

main()