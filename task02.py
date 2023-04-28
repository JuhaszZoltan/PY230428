from module import is_leap_year

print('2. feladat: Szökőév listázó')
firs_year:int = int(input('Kérem az egyik évszámot: '))
second_year:int = int(input('Kérem a másik évszámot: '))

if firs_year > second_year: firs_year, second_year = second_year, firs_year

leap_years:list[int] = []
for y in range(firs_year, second_year+1):
    if is_leap_year(y): leap_years.append(y)

if len(leap_years) == 0:
    print('Nincs szökőév a megadott tartományban!')
else:
    print(end='Szökőévek: ')
    for y in leap_years[:-1]: print(end=f'{y}; ')
    print(leap_years[-1])
