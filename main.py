from turtle import *
n = int(input("Сколько сторон у многоугольника? "))
for i in range(n):
 forward(100)
 left(360//n)
