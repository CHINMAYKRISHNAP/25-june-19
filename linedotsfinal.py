Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as tt
a1=tt.Turtle()
colors=['red','blue','green']
dot_distance=10
width=10
height=15
a1.penup()
for x in range(height):
    a1.pencolor(colors[x%3])
    for i in range(width):
        a1.dot()
        a1.forward(dot_distance)
    a1.forward(dot_distance*width)
    a1.right(90)
    a1.forward(dot_distance)
    a1.left(90)

tt.done()
