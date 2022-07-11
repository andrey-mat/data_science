""" Game - guess the number
"""
import numpy as np
number = np.random.randint(1, 101)

# Number of attempts
count = 0

while True:
    count+=1
    predict_number = int(input('Guess the number from 1 to 100:'))
    
    if predict_number > number:
        print('Number should be smaller!')
    elif predict_number < number:
        print('Number should be bigger!')
    else:
        print(f'You win! Number {number} guessed for {count} attempts') 
        break # end of cycle
