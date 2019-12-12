x = int(input("Введите номер месяца: "))
if x == 12 or x == 1 or x == 2:
    print("Зима")
elif 3 <= x <= 5:
    print("Весна")
elif 6 <= x <= 8:
    print("Лето")
elif 9 <= x <= 11:
    print("Осень")
else:
    print("Вы ввели несуществующий месяц")
