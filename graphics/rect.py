from graphics import *

win = GraphWin("Junha's the first program", 600, 500)

p1 = Point(100,100)
p2 = Point(300,100)

l1 = Line(p1, p2)
l1.draw(win)

p3 =Point(300,300)
l2 = Line(p2, p3)
l2.draw(win)


p4 =Point(100,300)
l3 = Line(p3, p4)
l3.draw(win)


l4 = Line(p4, p1)
l4.draw(win)

time.sleep(10)
