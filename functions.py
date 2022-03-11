import turtle as t
import math
t.speed(100)
def drawGraph(x,y,graphSize,graphSpaces,interval):
  t.color("black")
  t.pensize(.5)
  t.penup()
  t.goto(x,y - graphSize)
  t.pendown()
  for i in range (graphSpaces):
    if i%2 == 0:
      t.forward(graphSize)
    else:
      t.backward(graphSize)
    t.goto(t.xcor(), t.ycor() + interval )
  t.right(90)
  t.goto(x+graphSize,y)
  for i in range (graphSpaces):
    if i%2 == 0:
      t.forward(graphSize)
    else:
      t.backward(graphSize)
    t.goto(t.xcor() - interval, t.ycor() )
  t.forward(graphSize)
  t.goto(x,y)
  t.left(90)
  t.pensize(1)
def drawTri(a,b,c,interval):
  t.pensize(3)
  t.penup()
  t.goto(a[0]* interval , a[1] * interval)
  t.write('a')
  t.pencolor("red")
  t.pendown()
  t.goto(b[0]* interval , b[1] * interval)
  t.write('b')
  t.pencolor("blue")
  t.goto(c[0]* interval , c[1] * interval)
  t.write('c')
  t.pencolor("green")
  t.goto(a[0]* interval , a[1] * interval)
  t.pencolor("black")
def drawLine(b,changeX,changeY,interval,graphSize):
  t.penup()
  t.pensize(3)
  t.pencolor("purple")
  t.goto(0,b * interval)
  t.pendown()
  while t.ycor() >= (-1 * graphSize) - interval and t.ycor() <= graphSize - interval and t.xcor() >= (-1 * graphSize) - interval  and t.xcor() <= graphSize - interval :
  #for i in range (100):
    t.goto(t.xcor()+ (changeX * interval) , t.ycor() + (changeY * interval))

  t.goto(0,b* interval)
  while t.ycor() >= (-1 * graphSize) + interval and t.ycor() <= graphSize + interval and t.xcor() >= (-1 * graphSize) + interval and t.xcor() <= graphSize + interval:
  #for i in range (100):
    t.goto(t.xcor()- (changeX * interval) , t.ycor() - (changeY * interval))
  t.pencolor("black")
  t.penup() 

def linearLineData(x1,y1,x2,y2):
  m = (y2-y1) / (x2-x1)
  b = -1 * (m*x1) + y1
  return(m,b)

def writeLengths(x1,y1,x2,y2):
  t.penup()
  t.goto((x1+x2)/2,(y1+y2)/2)

  t.write(math.sqrt(((y1 - y2)** 2) + ((x2-x1)**2)))