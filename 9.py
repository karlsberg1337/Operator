dal = float(input('Введите дальность: '))

if dal > 28 and dal < 30:
    print('Попал')
elif dal >= 30:
    print('Перелет')
elif dal > 0 and dal <= 28:
    print('Недолет')
elif dal <=0:
    print('Свои не стреляй!!!')
