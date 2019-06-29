Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
>>> a1.forward(150)
>>> a1.right(90)
>>> a1.forward(150)
>>> a1.right(90)
>>> a1.forward(150)
>>> a1.right(90)
>>> tt.done()

== RESTART: C:/Users/exam/AppData/Local/Programs/Python/Python37-32/star.py ==
