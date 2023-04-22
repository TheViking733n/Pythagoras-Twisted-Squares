import turtle

SIZE = 500
COLORS = ['red', 'blue', 'green', 'yellow']
SQ_RATIO = .1
turtle.pensize(3)  # 3 pixels wide
turtle.Screen().bgcolor(0,0,0)  # black background
turtle.speed(0)  # fastest speed


n = SIZE // 2
corners = [(n, n), (n, -n), (-n, -n), (-n, n)]

def draw_square():
    turtle.penup()
    turtle.goto(corners[-1])
    turtle.pendown()
    for i in range(4):
        turtle.pencolor(COLORS[i])
        turtle.goto(corners[i])
    
    new_corners = []
    for i in range(4):
        x = corners[i][0] + (corners[(i+1)%4][0] - corners[i][0]) * SQ_RATIO
        y = corners[i][1] + (corners[(i+1)%4][1] - corners[i][1]) * SQ_RATIO
        new_corners.append((x, y))
    corners[:] = new_corners

def square_area():
    return (corners[0][0] - corners[2][0]) ** 2


while square_area() > 1:
    draw_square()


turtle.hideturtle()
turtle.mainloop()