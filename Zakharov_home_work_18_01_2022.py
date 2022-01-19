counter = 0
arr_numbers = []
while counter < 6:
    try:
        a = int(input("Введите число\n"))
        if int(a):
            arr_numbers.append(a)
            counter += 1
    except ValueError:
        print("Ошибка - вы ввели не число, повторите ввод;)\n")
for i in sorted(arr_numbers):
    print(int(i))