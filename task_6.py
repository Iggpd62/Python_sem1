ticket_number = input("Введите номер билета (6 цифр): ")

if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Ошибка: введен некорректный номер билета!")
else:
    first_half = int(ticket_number[:3])
    second_half = int(ticket_number[3:])
    if sum(int(digit) for digit in str(first_half)) == sum(int(digit) for digit in str(second_half)):
        print("Счастливый билет!")
    else:
        print("Несчастливый билет!")