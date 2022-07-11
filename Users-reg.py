def check_date(day, month, year):
    def is_leap(year):
        if year % 400 == 0: return True
        if year % 100 == 0: return False
        if year % 4 == 0: return True
        return False
    
    if type(day) is not int or type(month) is not int or\
       type(year) is not int: return False
    
    if not (1900 <= year <= 2022): return False
    if not (1 <= month <= 12): return False
    if not (1 <= day <= 31): return False
    if month in [4, 6, 9, 11] and day == 31: return False
    if month == 2 and day > 29: return False
    if is_leap(year) == False and month == 2 and day == 29: return False
    
    return True

def register(surname, name, date, middle_name=None, registry=None):
    if not check_date(*date): raise ValueError('Invalid Date!')
    if registry is None: registry = []
    registry.append((surname, name, middle_name, date[0], date[1], date[2]))
    return registry

  
reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
print(reg)
# [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]
 
#reg = register('Ivanov', 'Sergej', (24, 13, 1995))
# ValueError: Invalid Date!
