def holes_count(number):
  holes_dict = dict(zip(range(10), [1,0,0,0,1,0,1,0,2,1]))
  return sum([holes_dict[int(c)] for c in str(number)])
   

print(holes_count(123))
print(holes_count(8888))