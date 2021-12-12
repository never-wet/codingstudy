from graphics import *

def j1(sx,sy, ex, ey):
	a=Point(sx, sy)
	b=Point(ex, ey)
	l=Line(a,b)
	l.draw(win)
 f  df

size = 1000
win = GraphWin("Junha's the first program", size, size)


for d in range(0, size, 8):
	j1(0, d, d, size)


time.sleep(10)
# win.promptClose(win.getWidth()/2, 20)


