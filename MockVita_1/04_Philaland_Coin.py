def coin_count(num):
	i=0
	while(num>0):
		i += 1
		num = num >> 1
	return i

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        print(coin_count(int(input())))
        t -= 1

'''
6
10
20
30
45
100
500
'''
