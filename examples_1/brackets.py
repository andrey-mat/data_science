def brackets(line):
    stack = []
    try:
        for c in line:
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
    except IndexError:
        return False
    
    if stack == []:
        return True
    else:
        return False
            


print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False