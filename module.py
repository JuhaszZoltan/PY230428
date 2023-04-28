class Building:
    def __init__(self, row:str) -> None:
        splts:list[str] = row.strip().split(';')
        self.name:str = splts[0]
        self.city:str = splts[1]
        self.coutry:str = splts[2]
        self.height:float = float(splts[3].replace(',', '.'))
        self.floors:int = int(splts[4])
        self.built:int = int(splts[5])


def is_leap_year(year:int) -> bool:
    if year % 400 == 0: return True
    elif year % 4 == 0 and year % 100 != 0: return True
    else: return False