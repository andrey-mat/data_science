alphabet_str = 'AbcdefghijklmnopqrstuvwxyzA'

def letters_calc(s):
    return {c: s.lower().count(c) for c in s.lower()}

print(letters_calc(alphabet_str))