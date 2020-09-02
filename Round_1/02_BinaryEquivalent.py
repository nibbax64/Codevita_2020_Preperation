from itertools import combinations

to_bin = lambda num : str(bin(num))[2:]

def padd(num, len_):
	return '0'*(len_ - len(num))+num

def count(num):
	cnt = [0,0]
	cnt[1] = num.count("1")
	cnt[0] = num.count("0")
	return tuple(cnt)
def count_2(cnt, num):
	cnt = list(cnt)
	cnt[0] += num[0]
	cnt[1] += num[1]
	return tuple(cnt)

def is_equival(s):
	if(s[0] == s[1]):
		return True
	else:
		return False

if __name__ == "__main__":
	n = int(input())
	array = list(map(int, input().split()))
	max_ = len(to_bin(max(array)))
	array_b = list(map(to_bin, array))
	for i in range(n):
		array_b[i] = padd(array_b[i], max_)
	array = []
	for i in array_b:
		array.append(count(i))
#	print(array_b)
#	print(array)

	cnt = 0
	for i in range(1,n+1):
		comb = combinations(array,i)
		for c in comb:
#			print(f"comb:{c}")
			count_ = (0,0)
			for element in c:
				count_ = count_2(count_, element)
#			print(f"count_:{count_}")
			if(is_equival(count_)):
				cnt += 1
	print(padd(to_bin(cnt), max_),end="")
