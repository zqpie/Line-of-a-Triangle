from email.mime import base
from statistics import median
from functions import drawGraph, drawTri, linearLineData, drawLine, writeLengths
import turtle as t
import time
graphSize = 200
graphSpaces = 10
interval = graphSize / graphSpaces
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
        m = (vertexY - midpointY) / (vertexX - midpointY) 
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


    ##draw data to graph
    drawLine(b,1,m,interval,graphSize)
    writeLengths(0,0,5,5)
    if input("graph y/n ") == 'y':
        drawGraph(0,0,graphSize,graphSpaces,interval)
        drawGraph(0,graphSize,graphSize,graphSpaces,interval)
        drawGraph(-graphSize,0,graphSize,graphSpaces,interval)
        drawGraph(-graphSize,graphSize,graphSize,graphSpaces,interval)






finally:
    input('press enter to exit: ')