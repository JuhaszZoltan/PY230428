from module import *

buildings:list[Building] = []
rows:list[str] = open('legmagasabb.txt', 'r', encoding='utf-8').readlines()
for r in rows[1:]: buildings.append(Building(r))

print(f'3.2 feladat: Épületek száma: {len(buildings)} db')

sum_of_floors:int = 0
for b in buildings:
    sum_of_floors += b.floors
print(f'3.3 feladat. Emeletek összege: {sum_of_floors}')

highest_index:int = 0
for i in range(1, len(buildings)):
    if buildings[i].height > buildings[highest_index].height:
        highest_index = i
print('3.4 legmagasabb épület adatai:')
print(f'\tNév: {buildings[highest_index].name}')
print(f'\tVáros: {buildings[highest_index].city}')
print(f'\tOrszág: {buildings[highest_index].coutry}')
print(f'\tMagasság: {buildings[highest_index].height} m')
print(f'\tEmeletek száma: {buildings[highest_index].floors}')
print(f'\tÉpítés éve: {buildings[highest_index].built}')

WANTED_COUNTRY:str = 'Olaszország'
for b in buildings:
    if b.coutry == WANTED_COUNTRY:
        print('3.5 feladat: Van olasz épület az adatok között!')
        break
else: print('3.5 feladat: Nincs olasz épület az adatok között!')