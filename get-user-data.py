n = int(input('Please input number of people: '))
user_data = [input('Please enter the data for {} user: '.format(i+1)).split() for i in range(n)]
user_dict = dict(zip(range(1, n+1), user_data))
print(user_dict)
