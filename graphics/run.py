from graphics import *

X = 1000
Y = 1000
a=
win=GraphWin("Graph", X, Y)


for i in range(0, X, 20):
	start_pt = Point(0, i)
	end_pt = Point(i, Y)

	line1 = Line(start_pt, end_pt)
	line1.draw(win)

	start_pt = Point(X, i)
	end_pt = Point(i, 0)

	line2 = Line(start_pt, end_pt)
	line2.draw(win)


time.sleep(10)