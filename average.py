def average(nums):
    try:
        if type(nums) is not list:
            raise ValueError
    except ValueError:
        print('Arguments should me list')
        return
    try:
        return sum(nums) / len(nums)
    except TypeError:
        print('Arguments should be figures')
        return       

#Here we have lambda version as well
#average = lambda l: sum(l)/len(l)
print(average([1, 2, 10]))