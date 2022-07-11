# Напишите функцию lucky_ticket(), которая проверяет, является ли билетик счастливым.

# Памятка: билетик счастливый, если сумма первых трех цифр равна сумме последних трех цифр.

# На вход функция получает шестизначное число.

def lucky_ticket(ticket_number):
    res = False
    nums = [int(c) for c in str(ticket_number)]
    if sum(nums[:3]) == sum(nums[-3:]):
        res = True
    return res

print(lucky_ticket(111111))
print(lucky_ticket(123456))
