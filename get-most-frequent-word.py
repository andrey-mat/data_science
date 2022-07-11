# Модифицируем предыдущую задачу.
# Теперь необходимо написать функцию get_most_frequent_word, которое возвращает самое часто встречающееся слово в тексте.
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
# Текст, который можно использовать в качестве примера:

def get_unique_words(text):
    text = ''.join([c.lower() for c in text if c not in punctuation_list]).split()
    text.sort()
    return text

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    text = get_unique_words(text)
    counter = 0
    for word in text:
        if text.count(word) > counter: 
            counter = text.count(word)
            freq_word  = word
    return freq_word
    
print(get_most_frequent_word(text_example))