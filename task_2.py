number = input("Введите трехзначное число: ")

if len(number) != 3 or not number.isdigit():
    print("Ошибка: введено не трехзначное число!")
else:
    number = int(number)
    sum_of_digits = 0

    while number > 0:
        digit = number % 10
        sum_of_digits += digit
        number //= 10

    print("Сумма цифр трехзначного числа:", sum_of_digits)