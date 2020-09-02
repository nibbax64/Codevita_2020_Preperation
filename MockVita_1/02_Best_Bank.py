def bank_Interest(p, list_):
    interest = 0
    for i in list_:
        interest += (p*(i[1]/1200)*(1+(i[1]/1200))**(i[0]*12))/((1+(i[1]/1200))**((i[0]*12)-1))
    return interest

if __name__ == "__main__":
    p = float(input())
    t = float(input())
    temp = 0
    i1, i2 = [], []
    n = int(input())
    for i in range(n):
        i1.append(list(map(float, input().split())))
    n = int(input())
    for i in range(n):
        i2.append(list(map(float, input().split())))
    if(bank_Interest(p, i1) > bank_Interest(p, i2)):
        print("Bank B")
    else:
        print("Bank A")
