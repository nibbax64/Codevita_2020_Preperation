def isPrime(num):
    for i in range(2, (num//2)+1):
        if(num % i == 0):
            return False
    return True

def check(list_, num):
    sum_ = 0
    for i in list_:
        sum_ += i
        if(sum_ == num):
            return 1
        else:
            if(sum_ > num):
                return 0            
    return 0

def count_ins(num):
    prime_list = [2]
    ctr = 0
    for i in range(3, num+1):
        if(isPrime(i)):
            ctr += check(prime_list, i)
            prime_list.append(i)
    return ctr

if __name__ == "__main__":
    n = int(input())
    if(n > 2):
        print(count_ins(n))
