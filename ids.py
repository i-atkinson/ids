from datetime import datetime
from math import floor

def ids(dt):
    
    year = dt.year
    millenium = (year // 1000) + 1

    start_of_year = datetime(year,1,1)
    end_of_year = datetime(year,12,31)

    year_fraction = (dt - start_of_year) / (end_of_year - start_of_year)
    year_fraction = min(0.999,year_fraction)
    year_fraction = max(0.0,year_fraction)
    year_fraction = floor(year_fraction*1000)

    year = str(year)[-3:]
    
    check_number = 0

    ids_str = '{}.{}.{}.M{}'.format(check_number,year_fraction,year,millenium)
    
    return ids_str

def ids_now(): return ids(datetime.now())

if __name__=='__main__':
    print(ids_now())

