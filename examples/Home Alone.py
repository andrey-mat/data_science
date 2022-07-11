from turtle import *
from random import *

def stars(count = 1000, color = 'white'):
    for _ in range(count):
        penup()
        size = randrange(1,5)
        goto(randrange(-size_x//2, size_x//2), randrange(-size_y//2 + 10 * (window_space + window_size) + window_space, size_y//2))
        pendown()
        dot(size,color)
    
def building(left_x, right_x, top, color='blue'):
    bottom = -size_y
    penup()
    pencolor(color)
    fillcolor(color)
    goto(left_x, top)
    setheading(0)
    pendown()
    
    begin_fill()
    goto(right_x, top)
    goto(right_x, bottom)
    goto(left_x, bottom)
    goto(left_x, top)
    end_fill() 

def buildings(color='blue'):
    penup()
    fillcolor(color)
    goto(x_cor[0], y_cor[0])
    pendown()
    fillcolor(color)
    begin_fill()
    i = 1
    for i in range(len(x_pos)):
        if y_cor[i] == y_cor[i-1]:
            goto(x_cor[i], y_cor[i])
        else:
            goto(x_cor[i], y_cor[i-1])
            goto(x_cor[i], y_cor[i])
    goto(size_x //2, y_cor[i])
    goto(size_x //2, -size_y//2)
    goto(-size_x //2, -size_y//2)
    goto(-size_x //2, y_cor[0])
    end_fill()

def window(x, y, color='white'):
    penup()
    goto(x_cor[x] + window_space, y_cor[x] - y*(window_space + window_size) - window_space)
    pendown()
    fillcolor(color)
    begin_fill()
    setheading(0)
    for i in range(4):
        forward(window_size)
        right(90)
    end_fill()
          

size_x = 1270; size_y = 710
Screen().setup(1270, 710)
Screen().bgcolor('darkblue')
buildings_win = (2, 3, 4) # number of windows in buildings
window_size = 10
window_space = 10
speed(0)
hideturtle()

#new coordinates

x = -size_x //2

x_pos = []
y_pos = []
x_cor = []
y_cor = []

#set for first
height = randint(10,32)
y = -size_y //2 + height * (window_space + window_size) + window_space
x_pos.append(0); y_pos.append(height)
x_cor.append(x); y_cor.append(y)
i = j = 1
while x < size_x // 2:
    length = choice(buildings_win)
    if i == 1 and length == 4:
        length = 3
    for j in range(length):
        x += window_space + window_size
        if x >= size_x // 2:
            break        
        y = -size_y //2 + height * (window_space + window_size) + window_space
        x_pos.append(i)
        y_pos.append(height)
        x_cor.append(x)
        y_cor.append(y)
        i += 1
    x += window_space
    height = randint(10,20)
    if x >= size_x // 2:
        break
    
stars(200)
buildings()

print(x_pos)
print(y_pos)
print(x_cor)
print(y_cor)
         

wind_dens = 10 # 1 out of x
dens = [False for i in range(wind_dens - 1)]
dens.append(True)
for i in range(len(x_pos)):
    for j in range(y_pos[i] - 1):
        if choice(dens):
            window(i,j)
    

    



