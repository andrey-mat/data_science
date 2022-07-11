def yes_no(str):
    while True:
        print(str)
        s = input().upper()
        if s == 'ДА' or s == 'Д' or s == 'Y' or s == 'YES' or s == '1':
            return True
        if s == 'НЕТ' or s == 'Н' or s == 'N' or s == 'NO' or s == '0':
            return False

def get_digit(str):
    while True:
        print(str)
        s = input()
        if not s.isdigit():
            continue
        else:
            return int(s)

def caesar (s, method, language, step):
    code_sign = 2 * method -1 # + или - 
    
    if language == 1:
        lan_step = 26
        low_alph = eng_lower_alphabet
        up_alph = eng_upper_alphabet
    elif language == 0:
        lan_step = 32
        low_alph = rus_lower_alphabet
        up_alph = rus_upper_alphabet        
       
    s = [c for c in s]
    for i in range(len(s)):
        if s[i].isalpha() is True:
            if s[i] in low_alph:
                s[i] = low_alph[(low_alph.index(s[i]) + step * code_sign) % lan_step]
            elif s[i] in up_alph:
                s[i] = up_alph[(up_alph.index(s[i]) + step * code_sign) % lan_step]        
    s = ''.join(s)
    return s

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


method = yes_no('1 - Шифрование, 0 - Дешифрование')
language = yes_no('1 - Английский, 0 - Русский')
#step = get_digit('Введите величину сдвига')

print()
print('Введите текст')
s = input()

for step in range(0, 26):
    s1 = caesar(s, method, language, step)
    print(step, '-', s1)

