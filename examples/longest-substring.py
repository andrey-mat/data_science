def longest_sub(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    prev_c = s[0]
    lengths = []
    counter = 1    
    for i in range(1, len(s)):
        if s[i] == prev_c:
            counter += 1
        else:
            prev_c = s[i]
            lengths.append(counter)
            counter = 1
    return max(lengths)

print(longest_sub("adddaabaa"))
print(longest_sub("a"))
print(longest_sub("abbc"))
print(longest_sub(""))