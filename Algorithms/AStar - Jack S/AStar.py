import os
import pygame as pg
from pygame.locals import *
import tkinter as tk
import time
import math

# Constants - determine the size of the grid, and the size of the squares
ROW_COUNT = 30
COLUMN_COUNT = 58
B_SIZE = 30

SHOW_VISUAL = False

GRID_WIDTH = B_SIZE * COLUMN_COUNT + COLUMN_COUNT
GRID_HEIGHT = B_SIZE * ROW_COUNT + ROW_COUNT


# Priority queue class used for open list
class PriorityQueue(object):
    def __init__(self):
        self.itemList = []

    def __str__(self):
        return str([i.pos for i in self.itemList])

    def addToQueue(self, item):
        self.itemList.append(item)

    def getFromQueue(self):
        itemGot = self.itemList.pop(0)
        return itemGot

    def getLen(self):
        return len(self.itemList)

    def nodeList(self):
        return self.itemList

    def sort(self):  # Simple insertion sort
        isSorted = False
        while not isSorted:
            for selected in self.itemList[1:]:
                for nextItem in self.itemList[:self.itemList.index(selected)]:
                    if selected.f >= nextItem.f:
                        pass
                    if selected.f < nextItem.f:
                        self.itemList.remove(selected)
                        self.itemList.insert(self.itemList.index(nextItem),
                                             selected)
                        break

            isSorted = True


class Node(object):
    def __init__(self, parent, position):
        self.parent = parent  # Node object that this one was created from
        self.pos = position  # Coords

        self.g = 0  # Distance from start node 'cost'
        self.h = 0  # Heuristic function (estimated distance from end)
        self.f = 0  # Sum of g and h

    def __eq__(self, otherNode):  # Usage example: if nodeObject1 == nodeObject2
        return self.pos == otherNode.pos  # Compares positions

    def __str__(self):
        printout = ''
        printout += "G: " + str(self.g)
        printout += "H: " + str(self.h)
        printout += "F: " + str(self.f)
        printout += "\n"
        return printout


def aStar(grid, start, end):
    startNode = Node(None, start)
    endNode = Node(None, end)

    # Initialise open and closed lists
    oList = PriorityQueue()
    cList = []

    # 1) Add starting node to open list
    oList.addToQueue(startNode)

    # 2) Loop until end
    running = True
    while oList.getLen() > 0 and running:
        #time.sleep(0.1)
        goalFound = False
        # a) Look for lowest F cost node in open list
        currentNode = oList.getFromQueue()

        #print(currentNode)

        # b) Switch to closed list
        cList.append(currentNode)

        # If found goal
        if currentNode == endNode:
            lightSquare((255, 0, 0), currentNode.pos)
            path = []
            currentNode = currentNode
            while currentNode:
                path.append(currentNode)
                currentNode = currentNode.parent
            path.reverse()

            running = False
            goalFound = True
            continue

        if SHOW_VISUAL:
            lightSquare((255, 140, 0), currentNode.pos)

        # Generate child nodes
        childNodes = []
        # Adjacent squares
        # Top one allows diagonals, bottom doesn't
        for pos in [(0, -1), (0, 1), (1, -1), (1, 1), (1, 0), (-1, -1), (-1, 1),
                    (-1, 0)]:
            #for pos in [(0,-1),(0,1),(1,0),(-1,0)]:
            newCoords = (
                currentNode.pos[0] + pos[0], currentNode.pos[1] + pos[1])
            # Check within boundaries
            if newCoords[0] > COLUMN_COUNT or newCoords[0] < 1 or \
                    newCoords[1] > ROW_COUNT or newCoords[1] < 1:
                continue
            # Check if walkable
            if grid[newCoords[1] - 1][newCoords[0] - 1] == 1:
                continue

            # Check if goes through a wall (So can't move diagonally through
            # a diagonal wall)
            if pos in [(1, -1), (1, 1), (-1, -1), (-1, 1)]:
                xCheck = currentNode.pos[0] + pos[0] - 1
                yCheck = currentNode.pos[1] + pos[1] - 1

                if xCheck >= len(grid[0]) or yCheck >= len(grid):
                    continue

                if currentNode.pos[1] == 0 or currentNode.pos[0] == 0:
                    continue

                if grid[yCheck][currentNode.pos[0] - 1] == 1\
                        and grid[currentNode.pos[1] - 1][xCheck] == 1:
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
            if child.pos[0] == currentNode.pos[0] or \
                    child.pos[1] == currentNode.pos[1]:
                child.g = currentNode.g + 1.05
            else:
                child.g = currentNode.g + 1.5  # Diagonals 'cost' more

            child.h = math.sqrt(((child.pos[0] - endNode.pos[0]) ** 2) + (
                    (child.pos[1] - endNode.pos[1]) ** 2))
            child.f = child.g + child.h

            # If already on open list, checks to see if new node costs less
            """For ... in range is - from my testing - a better method of 
            iterating through the open list than for ... in list, as for .. in 
            list would sometimes end up removing the wrong node from the list, 
            therefore breaking the algorithm.

            """

            for currentIndex in range(0, oList.getLen()):
                try:
                    node = oList.itemList[currentIndex]
                except IndexError:
                    break
                if child == node and child.g > node.g:  # Compares based on g
                    continue
                elif child == node and child.g <= node.g:
                    del oList.itemList[currentIndex]
                    currentIndex -= 1
                    continue

            oList.addToQueue(
                child)  # Adds child node to open list to be processed

            if SHOW_VISUAL:
                lightSquare((255, 255, 0), child.pos)  # Lights up child nodes

        oList.sort()  # Sorts only after all children have been added

    if goalFound:  # if there is a route to end
        for node in path:  # Shows route in green
            lightSquare((0, 255, 0), node.pos)
            time.sleep(0.01)
        time.sleep(5)

    smallFont = pg.font.SysFont('Verdana', 36)  # Sets size and font of text
    # Renders text, ready for display
    restart = smallFont.render('Press enter to restart', True, (220, 220, 220))

    # Centers text on screen
    restartTextRect = restart.get_rect(
        center=(GRID_WIDTH // 2, GRID_HEIGHT // 2))
    transparentOverlay = pg.Surface((GRID_WIDTH, GRID_HEIGHT))
    transparentOverlay.set_alpha(175)  # Sets transparency of surface object
    pg.draw.rect(transparentOverlay, (0, 0, 0), transparentOverlay.get_rect())
    screen.blit(transparentOverlay, (0, 0))

    if not goalFound:  # If no route was found
        restartTextRect.y += 76  # Adds slight offset to line up with grid

        largeFont = pg.font.SysFont('Verdana', 72)
        noRoute = largeFont.render('No route available!', True, (220, 220, 220))

        noRouteTextRect = noRoute.get_rect(
            center=(GRID_WIDTH // 2, GRID_HEIGHT // 2))
        noRouteTextRect.y -= 11  # Adds slight offset to line up with grid
        screen.blit(noRoute, noRouteTextRect)

    pg.display.update()
    saveMap(grid)

    screen.blit(restart, restartTextRect)
    pg.display.update()

    done = True
    while done:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    done = False
    main()


def coordToXY(coord):
    # Converts grid coords to pygame pixel coords
    x = (coord[0] - 1) * (B_SIZE + 1)
    y = (coord[1] - 1) * (B_SIZE + 1)
    return x, y


def lightSquare(colour, coord):  # Procedure for colouring grid squares
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            quit()
    x, y = coordToXY(coord)  # Converts x y coords to pixel values
    rect = pg.Rect(x, y, B_SIZE, B_SIZE)
    pg.draw.rect(screen, colour, rect)
    pg.display.update()


def getMouseCoords():  # Retrieves mouse coords and converts to grid x y values
    x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
    newX = math.ceil(x / (B_SIZE + 1))
    newY = math.ceil(y / (B_SIZE + 1))
    return (newX, newY)


def drawing(grid):
    timer = 0
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
            if event.type == MOUSEBUTTONUP:
                if event.button == 3:
                    if timer == 0:
                        timer = (1 / 60)  # 1/60 because clock runs at 60fps
                        nextFrame = 0
                    if 0 < timer < 0.25 and nextFrame == 1:
                        # If two clicks are detected within 0.25s, double click registered
                        blankScreen(grid)  # Clears screen
                        timer = 0

        if pg.mouse.get_pressed()[0]:  # MB1 (left mouse button) draws 'maze'
            coords = getMouseCoords()
            grid[coords[1] - 1][coords[0] - 1] = 1  # Changes in 2D grid array
            lightSquare((0, 0, 0), coords)

        elif pg.mouse.get_pressed()[2]:  # MB2 (right) erases drawing
            coords = getMouseCoords()
            grid[coords[1] - 1][coords[0] - 1] = 0  # Changes in 2D grid array
            lightSquare((255, 255, 255), coords)

        if timer != 0:
            timer += (1 / 60)  # adds 1/60 every loop
        if timer >= 0.5:
            timer = 0

        nextFrame = 1  # nextFrame check prevents clicks being registered as two
        clock.tick(60)


def createNode(colour):  # Procedure for creating start/end nodes
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
                if grid[coords[1] - 1][
                    coords[0] - 1] != 0:  # If selected node is impassable
                    continue
                return coords

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    drawing = False

        clock.tick(60)


def blankScreen(grid):  # Procedure for redrawing a blank screen
    yCoord = 0
    for y in grid:
        xCoord = 0
        for x in y:
            grid[yCoord][xCoord] = 0
            rect = pg.Rect(xCoord * (B_SIZE + 1), yCoord * (B_SIZE + 1), B_SIZE,
                           B_SIZE)
            pg.draw.rect(screen, (255, 255, 255), rect)
            xCoord += 1
        yCoord += 1
    pg.display.update()


def selectMap():  # Procedure for selecting from preset maps
    global grid

    def select(selection):
        global grid
        if selection == "blankMaze":
            grid = []
            master.destroy()  # Breaks mainloop
            return

        fPath = os.path.dirname(os.path.realpath(
            __file__)) + "\\Preset Maps" + "\\" + selection + ".txt"
        with open(fPath) as f:
            # list comprehension for grid; y[:-1] removes newline character
            grid = [[int(x) for x in y[:-1]] for y in f.readlines()]

        if len(grid[0]) < COLUMN_COUNT:
            for row in grid:
                row.extend([0 for i in range(0, COLUMN_COUNT - len(row))])

        elif len(grid[0]) > COLUMN_COUNT:
            for row in grid:
                row = row[:COLUMN_COUNT]

        if len(grid) < ROW_COUNT:
            grid.extend([[0 for i in range(0, COLUMN_COUNT)] for i in
                         range(0, ROW_COUNT - len(grid))])

        elif len(grid) > ROW_COUNT:
            grid = grid[:ROW_COUNT]

        master.destroy()  # Breaks mainloop

    # Realpath gets path to file, dirname gets directory of that path
    location = os.path.dirname(os.path.realpath(__file__)) + "\\Preset Maps"

    optionsList = [file[:-4] for file in os.listdir(location)]

    master = tk.Tk()
    selectText = tk.Label(master, text="Select Preset Map",
                          font=("Verdana", 30))
    selectText.pack(side=tk.TOP)

    oDict = { }  # Dictionary used to hold the buttons

    # Sets up buttons from optionList, can be used for any number of options
    for option in optionsList:
        oDict[option] = tk.Button(master, text=option, font=("Verdana", 15))
        oDict[option].config(command=lambda opt=option: select(opt))
        oDict[option].pack(side=tk.TOP, fill=tk.X)

    master.mainloop()

    return grid


def saveMap(grid):  # Procedure for saving maps
    def no():
        master.destroy()

    def yes(grid):
        master.destroy()
        global name

        def readText(nameBox):
            global name
            name = nameBox.get()
            if len(
                    name) < 1:  # If no name has been entered, will not break loop
                return
            master2.destroy()

        master2 = tk.Tk()

        selectText = tk.Label(master2, text="Enter Map Name",
                              font=("Verdana", 30))
        selectText.pack(side=tk.TOP)

        nameBox = tk.Entry(master2)
        nameBox.pack()

        getText = tk.Button(master2, text="Save Map", font=("Verdana", 15))
        getText.config(command=lambda box=nameBox: readText(box))
        """If passing variables (nameBox) to lambda functions, rather than 
        constants, it seems to be required that you declare a new variable 
        inside of the function (box = nameBox), otherwise the button will do 
        nothing.

        """
        getText.pack(side=tk.BOTTOM, fill=tk.X)

        master2.mainloop()

        filepath = os.path.dirname(
            os.path.realpath(__file__)) + "\\Preset Maps" + "\\" + name + ".txt"

        gridString = ''  # Constructing grid string for txt file
        for y in grid:
            for x in y:
                gridString += str(x)
            gridString += '\n'

        mapFile = open(filepath, "w")
        mapFile.write(gridString)
        mapFile.close()

    master = tk.Tk()
    saveText = tk.Label(master, text="Save Map?", font=("Verdana", 30))
    yesButton = tk.Button(master, text="Yes", font=("Verdana", 15))
    yesButton.config(command=lambda g=grid: yes(g))
    noButton = tk.Button(master, text="No", font=("Verdana", 15))
    noButton.config(command=no)
    saveText.pack(side=tk.TOP)
    yesButton.pack(side=tk.BOTTOM, fill=tk.X)
    noButton.pack(side=tk.BOTTOM, fill=tk.X)
    master.mainloop()


def main():
    background_colour = (0, 0, 0)
    screen.fill(background_colour)
    grid = selectMap()
    yCoord = 0
    if grid != []:
        for y in grid:
            xCoord = 0
            yCoord += 1
            for x in y:
                xCoord += 1
                if x == 0:  # If walkable
                    lightSquare((255, 255, 255), (xCoord, yCoord))
                if x == 1:  # If not walkable
                    lightSquare((0, 0, 0), (xCoord, yCoord))
    else:
        rowNum = 1
        xCoord = 0
        yCoord = 0
        index = 0
        while rowNum <= ROW_COUNT:
            xCoord = 0
            yCoord += 1
            grid.append([])
            columnNum = 1
            while columnNum <= COLUMN_COUNT:
                xCoord += 1
                lightSquare((255, 255, 255), (xCoord, yCoord))
                grid[index].append(0)
                columnNum += 1
            index += 1
            rowNum += 1

    pg.display.set_caption('A* Pathfinding Algorithm Visualisation')
    pg.display.update()

    drawing(grid)
    startCoords = createNode((0, 255, 0))
    lightSquare((0, 255, 0), startCoords)
    endCoords = createNode((255, 0, 0))
    lightSquare((255, 0, 0), endCoords)

    aStar(grid, startCoords, endCoords)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False

    pg.quit()
    quit()


if __name__ == "__main__":  # If program is run as a script, this will run
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    grid = [[0 for i in range(1, COLUMN_COUNT)] for i in range(1, ROW_COUNT)]

    main()
