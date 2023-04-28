print('1. feladat: kisebb-nagyobb meghatározása')
firs_number:int = int(input('Kérem az első számot: '))
second_number:int = int(input('Kérem a második számot: '))

if firs_number == second_number:
    print('A két szám egyenlő.')
elif firs_number > second_number:
    print(f'A nagyobb szám {firs_number}, a kisebb {second_number}.')
else:
    print(f'A nagyobb szám {second_number}, a kisebb {firs_number}.')