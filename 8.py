year = int(input('Введите: '))

if year % 4 == 0:
        if year % 100 != 0:
            print('Год високосный')
        else:
            if year % 400 == 0:
                print('Год  високосный')
            else:
                print('Год не високосный')
else:
        print('Год не високосный')
