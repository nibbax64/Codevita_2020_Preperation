def rule_1(num):
    ll = []
    while(num > 0):
        ll.append(num%10)
        num = num//10
    return ((max(ll)*11 + min(ll)*7)%100)

def rule_2(ll):
    dat = {'even':{}, 'odd':{}}
    for i in range(1, len(ll),2):
        if(str(ll[i]//10) not in dat['even'].keys()):
            dat['even'][str(ll[i]//10)] = 1
        else:
            dat['even'][str(ll[i]//10)] += 1
    for i in range(0, len(ll),2):
        if(str(ll[i]//10) not in dat['odd'].keys()):
            dat['odd'][str(ll[i]//10)] = 1
        else:
            dat['odd'][str(ll[i]//10)] += 1
    count_ = 0
    for i in dat.values():
        for j in i.values():
            if(j == 2):
                count_ += 1
            elif(j > 2):
                count_ += 2
            else:
                continue
                
    print(count_)

if __name__ == "__main__":
    l1 = list(map(int, input().split()))
    l2 = []
    for i in l1[1:]:
        l2.append(rule_1(i))
    rule_2(l2)