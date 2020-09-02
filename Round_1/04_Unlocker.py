'''
5 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
3 2 1
'''
def clockwise(matrix, ini_r, ini_c, lim_r, lim_c):
	i,j = ini_r,ini_c
	store = matrix[i][j]

#	print(f"[{i},{j}]")
	#--col_1--
	for i in range(ini_r, lim_r-1):
		matrix[i][j] = matrix[i+1][j]
	
	i += 1
#	print(f"[{i},{j}]")
	#--row_n--
	for j in range(ini_c, lim_c-1):
		matrix[i][j] = matrix[i][j+1]

	j += 1
#	print(f"[{i},{j}]")
	#--col_n--
	for i in range(lim_r-1, ini_r, -1):
		matrix[i][j] = matrix[i-1][j]

	i -= 1
#	print(f"[{i},{j}]")
	#--row_1--
	for j in range(lim_c-1, ini_c, -1):
		matrix[i][j] = matrix[i][j-1]

#	j -= 1
#	print(f"[{i},{j}]")
	matrix[i][j] = store

	return matrix

def anticlockwise(matrix, ini_r, ini_c, lim_r, lim_c):

	i,j = ini_r,ini_c
	store = matrix[i][j]

#	print(f"[{i},{j}]")
	#--row_1--
	for j in range(ini_c, lim_c-1):
		matrix[i][j] = matrix[i][j+1]

	j += 1
#	print(f"[{i},{j}]")
	#--col_n--
	for i in range(ini_r, lim_r-1):
		matrix[i][j] = matrix[i+1][j]

	i += 1
#	print(f"[{i},{j}]")
	#--row_n--
	for j in range(lim_c-1, ini_c, -1):
		matrix[i][j] = matrix[i][j-1]

	j -= 1
#	print(f"[{i},{j}]")
	#--col_1--
	for i in range(lim_r-1, ini_r, -1):
		matrix[i][j] = matrix[i-1][j]

	#i -= 1
#	print(f"[{i},{j}]")
	matrix[i][j] = store
	return matrix

def unlock(matrix,m,n,rot):
	ini_r, ini_c, lim_r, lim_c = 0,0,m,n
	lev = 1
	for i in rot:
		if(lev%2 != 0):
			for j in range(i):
				matrix = anticlockwise(matrix,ini_r,ini_c,lim_r,lim_c)
				print_matrix(matrix,m,n)
				print("-"*10)
		else:
			for j in range(i):
				matrix = clockwise(matrix,ini_r,ini_c,lim_r,lim_c)
				print_matrix(matrix,m,n)
				print("-"*10)

		#lev += 1
		ini_r, ini_c = ini_r+1, ini_c+1
		if ini_r==lim_r and ini_c==lim_c:
			break
		else:
			lim_r, lim_c = lim_r-1, lim_c-1
		lev +=1
	return matrix

def print_matrix(matrix, m, n):
	for i in range(m):
		for j in range(n):
			print(f"{matrix[i][j]}\t", end="")
		print()
	return

if __name__ == "__main__":

	m,n = input().split()
	m,n = int(m),int(n)
	locked = []
	for i in range(m):
		inp = list(map(int, input().split()))
		locked.append(inp)
	rot = list(map(int, input().split()))

#	print_matrix(locked, m, n)
#	matrix = anticlockwise(locked,0,0,m,n)
#	print_matrix(locked, m, n)
#	matrix = clockwise(locked,0,0,m,n)
#	print_matrix(locked, m, n)

	locked = unlock(locked,m,n,rot)
	print_matrix(locked, m, n)
