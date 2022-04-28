import pygame as pg
from pygame.locals import *
import tkinter as tk
import time
import math

GRID_WIDTH = 777
GRID_HEIGHT = 851
B_SIZE = 36

class PriorityQueue(object):
    def __init__(self):
        self.itemList = []

    def __str__(self):
        return str([i.pos for i in self.itemList])

    def addToQueue(self, item):
        self.itemList.append(item)
##        self.sort()

    def getFromQueue(self):
        itemGot = self.itemList.pop(0)
        return itemGot

    def getLen(self):
        return len(self.itemList)

    def nodeList(self):
        return self.itemList
        
    def sort(self):
        maxIndex = len(self.itemList) - 1
        isSorted = False
        while not isSorted:
            for selected in self.itemList[1:]:
                for nextItem in self.itemList[:self.itemList.index(selected)]:
                    if selected.f >= nextItem.f:
                        pass
                    if selected.f < nextItem.f:
                        self.itemList.remove(selected)
                        self.itemList.insert(self.itemList.index(nextItem), selected)
                        break
                        
            isSorted = True

class Node(object):
    def __init__(self, parent, position):
        self.parent = parent
        self.pos = position
        
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, otherNode):
        return self.pos == otherNode.pos

    def __str__(self):
        return str(self.pos)
        
def aStar(grid, start, end):
    startNode = Node(None, start)
    endNode = Node(None,end)
    

    # Initialise open and closed lists
    oList = PriorityQueue()
    cList = []

    # 1) Add starting node to open list
    oList.addToQueue(startNode)

    # 2) Loop until end
    while oList.getLen() > 0:
        # a) Look for lowest F cost node in open list
        print(oList)
        currentNode = oList.getFromQueue()
        print(oList)
        input()

        
        # b) Switch to closed list
        cList.append(currentNode)

        # If found goal
        if currentNode == endNode:
            lightSquare((255,0,0), currentNode.pos)
            path = []
            currentNode = currentNode
            while currentNode:
                path.append(currentNode)
                currentNode = currentNode.parent
            path.reverse()

            return path

        # Generate child nodes
        childNodes = []
        # Adjacent squares
#        for pos in [(0,-1),(0,1),(1,-1),(1,1),(1,0),(-1,-1),(-1,1),(-1,0)]:
        for pos in [(0,-1),(0,1),(1,0),(-1,0)]:
            newCoords = (currentNode.pos[0] + pos[0], currentNode.pos[1] + pos[1])
            # Check within boundaries
            if newCoords[0] > len(grid[0]) or newCoords[0] < 1 or newCoords[1] > len(grid) or newCoords[1] < 1:
                continue
            # Check if empty space
            if grid[newCoords[1] - 1][newCoords[0] - 1] == 1:
                continue

            childNodes.append(Node(currentNode, newCoords))

        # c) For each of the adjacent nodes
        for child in childNodes:
            # If in closed list, ignore it
            inClosed = False
            for node in cList:
                if node == child:
                    inClosed = True
                    break
            
            if inClosed:
                continue
            
            # Calculate g, h, and f values
            child.g = currentNode.g + 10
            child.h = ((child.pos[0]-endNode.pos[0])**2)+((child.pos[1]-endNode.pos[1])**2)
            child.f = child.g + child.h
            
            for currentIndex in range(0, oList.getLen()):
                try:
                    node = oList.itemList[currentIndex]
                except IndexError:
                    break
                if child == node and child.g > node.g:
                    continue
                elif child == node and child.g <= node.g:
                    del oList.itemList[currentIndex]
                    currentIndex -= 1
                    continue

            oList.addToQueue(child)
            
            lightSquare((255,140,0), child.pos)
#            time.sleep(0.05)
        
        oList.sort()

def coordToXY(coord):
    x = (coord[0] - 1) * (B_SIZE + 1)
    y = (coord[1] - 1) * (B_SIZE + 1)
    return x,y

def drawSquare(x, y, blocked):
    if blocked == 0:
        colour = (255,255,255)
    if blocked == 1:
        colour = (0,0,0)
    rect = pg.Rect(x*(B_SIZE+1), y*(B_SIZE+1), B_SIZE, B_SIZE)
    pg.draw.rect(screen, colour, rect)

def lightSquare(colour, coord):
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            break
    x,y = coordToXY(coord)
    rect = pg.Rect(x, y, B_SIZE, B_SIZE)
    pg.draw.rect(screen, colour, rect)
    pg.display.update()

def getMouseCoords():
    x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
    newX = math.ceil(x / (B_SIZE + 1))
    newY = math.ceil(y / (B_SIZE + 1))
    return (newX,newY)

def drawing():
    clock = pg.time.Clock()
    drawing = True
    while drawing:
        for event in pg.event.get():
            if event.type == QUIT: 
                drawing = False
                pg.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    drawing = False
        if pg.mouse.get_pressed()[0]:
            coords = getMouseCoords()
            grid[coords[1] - 1][coords[0] - 1] = 1
            lightSquare((0, 0, 0), coords)

        elif pg.mouse.get_pressed()[2]:
            coords = getMouseCoords()
            grid[coords[1] - 1][coords[0] - 1] = 0
            lightSquare((255, 255, 255), coords)

        clock.tick(60)

def createNode(colour):
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT: 
                running = False
                pg.quit()
                quit()
            if event.type == MOUSEBUTTONUP:
                coords = getMouseCoords()
                return coords
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    drawing = False
        clock.tick(60)

grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
pg.init()
pg.font.init()
font = pg.font.SysFont('Verdana', 8)
screen = pg.display.set_mode((GRID_WIDTH,GRID_HEIGHT))
background_colour = (0,0,0)
screen.fill(background_colour)

yCoord = 0
for y in grid:
    xCoord = 0
    for x in y:
        drawSquare(xCoord, yCoord, x)
        xCoord += 1
    yCoord += 1
    
pg.display.set_caption('A* Pathfinding Algorithm Visualisation')
pg.display.update()

drawing()
startCoords = createNode((0,255,0))
lightSquare((0,255,0),startCoords)
endCoords = createNode((255,0,0))
lightSquare((255,0,0),endCoords)
print(grid)
for node in aStar(grid, tuple(startCoords), tuple(endCoords)):
    lightSquare((0,255,0), node.pos)
    time.sleep(0.1)

running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT: 
            running = False

pg.quit()
quit()
