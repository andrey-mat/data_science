def get_10(x, n):
    dig1 = x % 10
    dig2 = x // 10
    x10 = dig1 * 1 + dig2 * n
    return x10

def get_x(x, n):
    xn = []
    while x  >= n:
        xn.append(x % n)
        x = x // n
    xn.append(x)
    xn = [str(s) for s in xn]
    const10 = ['10', '11', '12', '13', '14', '15']
    const16 = ['A', 'B', 'C', 'D', 'E', 'F']

    for i in range(len(const10)):
        for j in range(len(xn)):
            if xn[j] == const10[i]:
                xn[j] = const16[i]
    xn = xn[::-1]
    xn = ''.join(xn)
    
    return xn
       
'''n = [32, 22, 16, 17]
total = 88

i = 2
while True:
    n10 = [get_10(x, i) for x in n]
    total10 = get_10(total, i)
    if total10 == sum(n10):
        break
    i += 1
'''

n = 513

print(get_x(n, 2))


