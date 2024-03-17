import turtle

b = 20
c = 15
a = 0
turtle.color('black')
turtle.begin_fill()
turtle.backward(0)
turtle.right(90)
turtle.backward(0)
turtle.left(90)
turtle.color('red', 'white')
while True:
    turtle.forward(c+b)
    turtle.left(c-b)
    c -= 6
    turtle.backward(b-c)
    turtle.left(150)
    turtle.left(b-c-c-c-c-b)
    turtle.right(c)
    b -= 5
    c -= 2
    turtle.backward(b - c)
    turtle.left(150)
    turtle.right(c)
    turtle.speed(30)
    turtle.forward(c + b)
    a += 1
    b += 10
    c += 7
    print(a)
    if a > 50:
        break


turtle.end_fill()
turtle.done()
