from math import sqrt
def distance_between_dots(x1, y1, x2, y2):
    try:
        coords = [x1, y1, x2, y2]  
        for c in coords:
            if type(c) is not int and type(c) is not float:
                raise ValueError
    except ValueError:
        print('Wrong coordinates!')
        return
        
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


print(distance_between_dots(1, 2, 4, 6))