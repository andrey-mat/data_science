from random import *

words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", 
              "история", "женщина", "развитие", "власть", "правительство", 
              "начальник", "спектакль", "автомобиль", "экономика", "литература", 
              "граница", "магазин", "председатель", "сотрудник", "республика", 
              "личность"]
guessed_letters = [] 

def yes_no(str):
    while True:
        print(str)
        s = input().upper()
        if s == 'ДА' or s == 'Д' or s == 'Y' or s == 'YES' or s == '1':
            return True
        if s == 'НЕТ' or s == 'Н' or s == 'N' or s == 'NO' or s == '0':
            return False

def get_word():
    return choice(words_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(f'Осталось {tries} попыток')
    return stages[tries]

def get_letter(s):
    global guessed_letters  
    while True:
        print(s)
        c = input()
        if len(c) > 1:
            continue
        if c.upper() in guessed_letters:
            print('Такая буква уже была')
            continue
        if c.isalpha() is True:
            return c.upper()
        

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = [c for c in word_completion]
    guessed = False                    # сигнальная метка
    global guessed_letters              # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    
    word = [c for c in word]
    saved_word = word.copy()
    print('Давайте играть в угадайку слов!')
    while tries >= 0:
        success_flag = 0
        print(display_hangman(tries))
        print(*word_completion)
        if tries == 0:
            break
        letter = get_letter('Введите букву')
        guessed_letters.append(letter)
        while letter in word:
            t = word.index(letter)
            word_completion[t] = letter
            word[t] = '*'
            success_flag += 1
        if '_' not in word_completion:
            break
        if success_flag > 0:
            continue       
        tries -= 1
        
    if tries > 0:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы проиграли!')
        print('Загаданное слово:')
        print(*saved_word)
                
while True:
    word = get_word()
    play(word)
    if yes_no('Хотите поиграть еще раз?') == False:
        break
    guessed_letters = []



