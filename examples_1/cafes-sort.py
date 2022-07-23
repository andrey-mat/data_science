ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)
print(cafes)

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
         
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.


# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes1 = sorted(ratings)
cafes1.sort(key=lambda t:t[1], reverse=True)
cafes1 = OrderedDict(cafes1)

for element in cafes:
    print(element, cafes[element] == cafes1[element])

print(cafes1==cafes)