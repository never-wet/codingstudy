from graphics import *

def j1(sx,sy, ex, ey):
	a=Point(sx, sy)
	b=Point(ex, ey)
	l=Line(a,b)
	l.draw(win)


size = 1000
win = GraphWin("Junha's the first program", size, size)


for d in range(0, size, 50):
	X = 0
	Y = 0
	r = size
	j1(X + 0, Y + d, X + d, Y + r)
	j1(X + d, Y + r, X + r, Y + r - d)
	j1(X + d, Y + 0, X + r, Y + d)
	j1(X + d, Y + 0, X + 0, Y + r - d)


r = 100
C = size / 2




for d in range(0, r + 1, 5):
	X = C - r
	Y = C - r
	j1(X + d, Y + 0, X + 0, Y + r - d)

	X = C
	Y = C - r
	j1( X + d, Y + 0, X + r , Y + d)

	X = 
	Y = 
	j1(X + 0, Y + d, X + d, Y + r)

	X = 
	Y = 
	j1(X + d, Y + r, X + r, Y + r - d)

time.sleep(100000)
# win.promptClose(win.getWidth()/2, 20)

