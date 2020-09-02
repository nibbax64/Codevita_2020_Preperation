def isPrime(num):
    for i in range(2, (num//2)+1):
        if(num % i == 0):
            return False
    return True

def combination(list_):
    comb_list = []
    for i in range(len(list_)):
        for j in range(len(list_)):
            if(i != j):
                temp = int("".join([str(list_[i]), str(list_[j])]))
                if(temp not in comb_list):
                    comb_list.append(temp)
    return comb_list

def fibo(num1, num2, t):
    temp = 0
    for i in range(t-1):
        temp = num1 + num2
        num1 = num2
        num2 = temp
    return num1

if __name__ == "__main__":
    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)
    if(n2 - n1 >= 35):
        prime_list = []
        for i in range(n1, n2+1):
            if(isPrime(i)):
                prime_list.append(i)
        comb_list = combination(prime_list)
        prime_list = []
        for i in comb_list:
            if(isPrime(i)):
                prime_list.append(i)
        max_, min_, len_ = max(prime_list), min(prime_list), len(prime_list)
        print(fibo(min_, max_, len_))
