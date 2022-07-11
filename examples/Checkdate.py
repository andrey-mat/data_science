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
        
print(check_date(18,9,1999))
print(check_date(29,2,2000))
print(check_date(29,2,2021))
print(check_date(13,13,2021))
print(check_date(13.5,12,2021))
# True
# True
# False
# False
# False