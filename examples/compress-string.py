s = 'aaabbccccdaa'
new_s = s[0]
i = 1
counter = 1
while i < len(s):
    if s[i] == s[i-1]:
        counter += 1
        i += 1
        continue
    new_s = new_s + str(counter) + s[i]
    i += 1
    counter = 1
if counter > 1:
    new_s = new_s + str(counter)
print(new_s)
    