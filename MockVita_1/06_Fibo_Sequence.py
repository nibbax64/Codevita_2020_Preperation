def fibo_list_dd(lim):
    n1, n2, temp = 0, 1, 0
    fibo = []
    for i in range(lim):
        fibo.append(n1%10)
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return fibo

def clean(list_):
    if(len(list_) == 1):
        return list_[0]
    else:
        return clean(list_[1::2])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        print(clean(fibo_list_dd(int(input()))))
