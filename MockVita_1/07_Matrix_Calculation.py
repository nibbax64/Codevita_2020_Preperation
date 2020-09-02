if __name__ == "__main__":
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    l, r = 0, 0
    for i in range(n):
        l += mat[i][i]
        r += mat[i][n-1-i]
    print(abs(l-r))
