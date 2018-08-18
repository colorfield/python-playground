# Draws a spiral
import turtle
steps = 50
angle = 45
t = turtle.Pen()
for x in range(steps):
    t.forward(x)
    t.left(angle)
