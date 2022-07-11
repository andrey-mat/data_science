from random import *
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

def again(question):
    while True:
        print(question)
        s = input().upper()
        if s == 'ДА':
            play()
        if s == 'НЕТ':
            break    

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как Вас зовут?')
name = input()
print(f'Привет, {name}')

stop = False
while True:
    if stop is True:
        break
    
    print('Какой Ваш вопрос?')
    question = input()
    print(choice(answers),'\n')
    
    while True:
        print('Хотите попробовать еще разок?')
        s = input().upper()
        if s == 'ДА':
            break
        if s == 'НЕТ':
            stop = True
            break
print()
print('Возвращайся, если возникнут вопросы!')