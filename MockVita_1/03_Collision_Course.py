def time(data):
    dist = 0
    time_ = []
    for i in data:
        time_.append(((i[0]**2 + i[1]**2)**(1/2))/i[2])
    return time_

def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num*factorial(num-1)

def combination(n, r):
    n, r = int(n), int(r)
    if(n >= r):
        return (factorial(n)/(factorial(n-r)*factorial(r)))
    else:
        return 1

if __name__ == "__main__":
    t = int(input())
    data = []
    for i in range(t):
        data.append(tuple(map(float, input().split())))
    data = time(data)
    count = {}
    for i in data:
        if(i not in count.keys()):
            count[i] = 1
        else:
            count[i] += 1
    for key in count.keys():
        count[key] = combination(count[key], 2)
    print(count)
    print(sum(count.values()))

'''
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
'''
