from random import *

def yes_no(str):
    while True:
        print(str)
        s = input().upper()
        if s == 'ДА' or s == 'Д' or s == 'Y' or s == 'YES' or s == '1':
            return True
        if s == 'НЕТ' or s == 'Н' or s == 'N' or s == 'NO' or s == '0':
            return False
        
def generate_password(length, chars):
    s = sample(chars, length)
    s = ''.join(s)
    return s

digits =  '0123456789'
low_let = 'abcdefghijklmnopqrstuvwxyz'
up_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym = '!#$%&*+-=?@^_.'
strange = 'il1Lo0O'

print('Количество паролей для генерации?')
n = int(input())

print('Длина одного пароля?')
l = int(input())

f_dig = yes_no('Включать ли цифры 0123456789?')
f_up = yes_no('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
f_low = yes_no('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
f_sym = yes_no('Включать ли символы !#$%&*+-=?@^_?')
f_str = yes_no('Исключать ли неоднозначные символы il1Lo0O?')

chars = digits * f_dig + up_let * f_up + low_let * f_low + sym * f_sym 
if f_str is True:
    for i in range(len(strange)):
        chars = chars.replace(strange[i],'')

for _ in range(n):
    print(generate_password(l, chars))

               
