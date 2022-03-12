from asyncore import write
from termios import CLNEXT
from functions import drawGraph, drawTri, linearLineData, drawLine, writeLengths, drawSquare
import math, turtle as t
graphSize = 200
graphSpaces = 10
interval = graphSize /graphSpaces
a=(0,15)
b=(15,0)
c=(0,0)## right angle
drawTri(a,b,c,interval)
drawSquare((a[0],a[1]/10),(b[0]/10,a[1]/10),(b[0]/10,b[1]),c,  interval)

## collect data
print('input lengths, type zero if you want to solve for that length')
hypotLength = float(input('hypot length: '))
aLength = float(input('a length: '))
bLength = float(input('b length: '))
sidesVal = [hypotLength,aLength,bLength]
sidesStr = ['hypot','a','b']
for i in range (3):
    if sidesVal[i] == 0:
        solveSide = sidesStr[i]
print (solveSide)

if solveSide == 'hypot':
    hypotLength = math.sqrt((aLength**2) + (aLength**2))
elif solveSide == 'a':
    aLength = math.sqrt(bLength ** 2) - (hypotLength ** 2) 
elif solveSide == 'b':
    bLength = math.sqrt(aLength ** 2) - (hypotLength ** 2) 
print(hypotLength,aLength,bLength)
t.penup()
t.goto(((a[0] + b[0]) /2 ) * interval, ((a[1] + b[1]) /2) * interval)
t.write(str(hypotLength))
t.goto(((c[0] + b[0]) /2 ) * interval, ((c[1] + b[1]) /2) * interval)
t.write(str(bLength))
t.goto(((c[0] + a[0]) /2 ) * interval, ((c[1] + a[1]) /2) * interval)
t.write(str(aLength))


input('done: ')
