import random
import time

a = 30
o = 30

shape_x = a // 4
shape_y = o // 4
shape_width = a // 2
shape_height = o // 2
x = random.randint(shape_x, shape_x + shape_width - 1)
y = shape_y

direction = "down"

while True:
    for i in range(a):
        for j in range(o):
            if i == 0 or i == a - 1:
                print('-', end='')
            elif j == 0 or j == o - 1:
                print('|', end='')
            elif (shape_x <= i < shape_x + shape_width) and (shape_y <= j < shape_y + shape_height):
                if i == y and j == x:
                    print('&', end='')
                else:
                    print(' ', end='')
            else:
                print(' ', end='')
        print()

    time.sleep(0.15)

    if direction == "down":
        y += 1
        if y == shape_y + shape_height:
            direction = "exit"
    elif direction == "exit":
        if x < shape_x + shape_width - 1:
            x += 1
        else:
            direction = "random"
    elif direction == "random":
        x = random.randint(shape_x, shape_x + shape_width - 1)
        y = shape_y
        direction = "down"
    print("\033c")
