"""Game - guess the number - VERSION 3
Computer will guess itself then figure out the number
"""

import numpy as np
    
def random_predict(number:int=1) -> int:
    """Random number guessing

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Number of attempt to guess
    """
    count = 0
    predict_range = [0, 100] # Low limit of seek range
    predict_number = (predict_range[0] + predict_range[1]) // 2 # Middle number to guess -- 50 for 1 attempt
    while True:
        count+=1        
        if number == predict_number:
            break # Exit if number figured out
        elif predict_number > number:
            predict_range[1] = predict_number # Update the high limit of seek range
            predict_number = (predict_range[0] + predict_range[1]) // 2 # Recalculate the number to seek
        else: # if predict_number < number
            predict_range[0] = predict_number # Update the low limit of seek range
            predict_number = (predict_range[0] + predict_range[1]) // 2 # Recalculate the number to seek
  
    return count

def score_game(random_predict) -> int:
    """Calculates average number of attempts to guess the number for 1000 iterations

    Args:
        random_predict (_type_): Function used for guessing

    Returns:
        int: Average number of attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'The algorithm guessed the number for average {score} attempts')
    return score


if __name__ == '__main__':
    # RUN
    score_game(random_predict)