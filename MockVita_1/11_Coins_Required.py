count = [0,0,0,0]
def rec_count(num):
    global count


def count_coin(num):
    for i in range(1, num+1):
        rec_count(i)
    count[0] = sum(count[1:])
    return count




if __name__ == "__main__":
    n = int(input())
    print(count_coin(n))
