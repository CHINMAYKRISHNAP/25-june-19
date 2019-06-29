>>> # draw a squace
>>> import turtle as tt
>>> a1=tt.Turtle()
>>> a1.forward(150)
>>> a1.roght(90)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a1.roght(90)
AttributeError: 'Turtle' object has no attribute 'roght'
>>> a1.right(90)
>>> a1.backward(150)
>>> a1.right(90)
>>> a1.backward(150)
>>> a1.right(90)
>>> a1.backward(150)
a1.right(90)
a1.backward(150)

