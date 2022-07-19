import pandas as pd

def get_experience(arg):
    #Check if string contains words 'month', 'year' etc.
    nums = [int(s) for s in arg.split() if s.isdigit()]
    if len(nums) == 2:
        return nums[0]*12 + nums[1]
    elif 'месяц' in arg:
        return nums[0]
    else:
        return nums[0]*12
    
    

if __name__ == '__main__':
    experience_col = pd.Series([
        'Опыт работы 8 лет 3 месяца',
        'Опыт работы 3 года 5 месяцев',
        'Опыт работы 1 год 9 месяцев',
        'Опыт работы 3 месяца',
        'Опыт работы 6 лет'
        ])
    experience_month = experience_col.apply(get_experience)
    print(experience_month)