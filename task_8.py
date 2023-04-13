n, m, k = map(int, input("Введите размеры шоколадки(n,m) и количество долек(k): ").split())

if k > n * m or k % n != 0 and k % m != 0:
    print("no")
else:
    print("yes")