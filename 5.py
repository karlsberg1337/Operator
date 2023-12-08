a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a < b+c and b < a+c and c < a+c:
    print('существует')
else:
    print('не существует')
