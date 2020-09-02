CONST = 1000000007
if __name__ == "__main__":
    t = int(input())
    n_t_m = []
    for i in range(t):
        n, tt, m = input().split()
        n, tt, m = int(n), int(tt), int(m)
        s = float(tt/m)
        print(int((s*CONST)+0.5))
