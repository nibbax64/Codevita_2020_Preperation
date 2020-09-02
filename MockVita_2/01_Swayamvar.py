def get_unpair(bride_q, groom_q):
    count_ = 0
    flag1,flag2 = True,True
    while(flag1):
        if(len(groom_q) > 0):
            j = 0
            ln = len(groom_q)
            flag2 = True
            while(flag2):
                    if(bride_q[0] == groom_q[0]):
                        count += 1
                        bride_q.pop(0)
                        groom_q.pop(0)
                        # print(bride_q.pop(0))
                        # print(groom_q.pop(0))
                        flag2 = False
                    else:
                        groom_q.append(groom_q.pop(0))
                        # print(bride_q)
                        # print(groom_q)
                        j += 1
                        
                    if(j == ln):
                        flag1, flag2 = False, False
                        break
        else:
            break
    return count_

if __name__ == "__main__":
    n = int(input())
    if(1<=n<=10**4):
        bride_q, groom_q = [], []
        inp = input().split()
        if(n == len(inp[0]) == len(inp[1])):
            for i in inp[0]:
                bride_q.append(i)
            for i in inp[1]:
                groom_q.append(i)
            print(n-get_unpair(bride_q, groom_q), end="")
    print()