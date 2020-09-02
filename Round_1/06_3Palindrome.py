def is_palindrome(inp, n):
	for i in range(n//2):
		if(inp[i] != inp[n-i-1]):
			return False
	return True

if __name__ == "__main__":
	inp = input()
	n = len(inp)
	print(is_palindrome(inp, n))
