s = int(input("Введите количество журавликов: "))

for i in range(s // 2 + 1):
    for j in range(s // 2 + 1):
        if i == j and i + j + i * 2 == s:  
            print("Петя:", i)
            print("Катя:", i * 2)
            print("Сережа:", j)
            exit()

print("Нельзя определить")