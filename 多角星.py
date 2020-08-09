import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed(100)
turtle.color('red', 'yellow')

# 准备填色
turtle.begin_fill()

# 走36次
for i in range(36):
    turtle.forward(400)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

# 填色
turtle.end_fill()

print('已完成')
turtle.done()
