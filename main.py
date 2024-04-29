import turtle

a = turtle.Screen()
t = turtle.Turtle()
for i in range(8):
 t.forward(100)
 t.left(45)
for i in range(8):
 t.forward(50)
 t.left(90)
 t.forward(20)
 t.left(180)
 t.forward(20)
 t.left(90)
 t.forward(50)
 t.left(45)
input("Нажми, чтоб закрыть программу")