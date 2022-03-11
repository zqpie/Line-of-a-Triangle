from email.mime import base
from statistics import median
from functions import drawGraph, drawTri, linearLineData, drawLine, writeLengths
import turtle as t
import time
graphSize = 200
graphSpaces = 10
interval = graphSize / graphSpaces

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

try:
    print("enter points of your triangle below: ")
    aCoords = (float(input('point A. x: ')),float(input('point A. y: ')))
    bCoords = (float(input('point B. x: ')),float(input('point B. y: ')))
    cCoords = (float(input('point C. x: ')),float(input('point C. y: ')))
    drawTri(aCoords,bCoords,cCoords,interval)
    mode = input('med/pb/alt ')
    if mode == 'med':
        medianVertexString = input('vertex? ') ## string name of median vertex
        ## convert name to points
        if medianVertexString == 'a':
            medianVertexCoords = aCoords
            medianBaseCoords = (bCoords, cCoords)
        elif medianVertexString == 'b':
            medianVertexCoords = bCoords
            medianBaseCoords = (aCoords, cCoords)
        elif medianVertexString == 'c':
            medianVertexCoords = cCoords
            medianBaseCoords = (bCoords, aCoords)
        ## get two points from base line
        basePoint1 = medianBaseCoords[0]
        basePoint2 = medianBaseCoords[1]
        ## calculate midpoint
        baseMidpoint = ((basePoint1[0] + basePoint2[0]) /2), ((basePoint1[1] + basePoint2[1]) /2)
        ## redifined for readability
        midpointX = float(baseMidpoint[0])
        midpointY = float(baseMidpoint[1])
        vertexX = medianVertexCoords[0]
        vertexY = medianVertexCoords[1]
        ## calculate equation
        m = (vertexY - midpointY) / (vertexX - midpointX) 
        b = -1 * (m *midpointX) + midpointY
    elif mode == 'alt':
        altitudeVertexString = input('Vertex? ')
        if altitudeVertexString == 'a':
            altitudeVertex = aCoords
            altitudeBase = [bCoords,cCoords]
        elif altitudeVertexString == 'b':
            altitudeVertex = bCoords
            altitudeBase = [aCoords,cCoords]
        elif altitudeVertexString == 'c':
            altitudeVertex = cCoords
            altitudeBase = [bCoords,aCoords]
        vertexX = altitudeVertex[0]
        vertexY = altitudeVertex[1]
        basePoint1 = altitudeBase[0]
        basePoint2 = altitudeBase[1]
        slopeBase = (basePoint2[1] - basePoint1[1]) / (basePoint2[0] - basePoint1[0])
        m = -1 / slopeBase
        b = -1 * (m*altitudeVertex[0]) + altitudeVertex[1]
    elif mode == 'pb':
        side = input('side (type the letters): ')
        sideCoords = []
        if 'a' in side:
            sideCoords.append(aCoords)
        if 'b' in side:
            sideCoords.append(bCoords)
        if 'c' in side:
            sideCoords.append(cCoords)
        point1 = sideCoords[0] ## break apart into two pairs of coords
        point2 = sideCoords[1]
        changeX = (point1[0] - point2[0]) 
        changeY = (point1[1] - point2[1])
        x1= point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        mBase = (y2 - y1) / (x2-x1)
        midpoint =  (x2 + x1) /2 , (y2 + y1) / 2 
        m = -1 / mBase # resiprical -
        b = -1 * (m *midpoint[0]) + midpoint[1]
    elif mode == 'dialate':
        ax = aCoords[0]
        ay = aCoords[1]
        bx = bCoords[0]
        by = bCoords[1]
        cx = cCoords[0]
        cy = cCoords[1]
        dialationPoint = (float(input('dialation X:' )), float(input('dialation Y: ')))
        k = float(input('enter scaleFactor: '))
        dx = dialationPoint[0]
        dy = dialationPoint[1]

        axp = (k * (ax - dx)) + dx 
        ayp = (k * (ay - dy)) + dy
        bxp = (k * (bx - dx)) + dx ### key: first letter is the point, second is x or y and p if it is prime(second triangle)
        byp = (k * (by - dy)) + dy
        cxp = (k * (cx - dx)) + dx
        cyp = (k * (cy - dy)) + dy
        apCoords = (axp,ayp)
        bpCoords = (bxp,byp)
        cpCoords = (cxp,cyp)
        drawTri(apCoords,bpCoords,cpCoords,interval)
    ##draw data to graph
    if mode != 'dialate':
        drawLine(b,1,m,interval,graphSize)
    #writeLengths(0,0,5,5)
    if input("graph y/n ") == 'y':
        drawGraph(0,0,graphSize,graphSpaces,interval)
        drawGraph(0,graphSize,graphSize,graphSpaces,interval)
        drawGraph(-graphSize,0,graphSize,graphSpaces,interval)
        drawGraph(-graphSize,graphSize,graphSize,graphSpaces,interval)
finally:
    input('press enter to exit: ')
