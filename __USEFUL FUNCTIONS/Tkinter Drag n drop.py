import tkinter

def addDraggable(widget):
    widget.bind("<B1-Motion>", lambda event : moveWidget(event, widget))
    widget.configure(cursor="hand2")

##Procedure for dragging and dropping widgets
def moveWidget(event, self):
    self.place(anchor=tk.CENTER, x=root.winfo_pointerx()-root.winfo_rootx(), y=root.winfo_pointery()-root.winfo_rooty())

##Procedure for detecting collsion between two labels
def checkCollision(event, self, selfID, target, itemName, itemIndex):
    Coords = [self.winfo_rootx(), self.winfo_rooty()] # Get coordinates of widget being dragged
    print(Coords)
    coordsOfTarget = [target.winfo_rootx(), target.winfo_rooty()] # Get coordinates of target widget
    print(coordsOfTarget)
    if coordsOfTarget[0] < Coords[0] + (self.winfo_width() / 4) <\
         coordsOfTarget[0] + target.winfo_width() and\
         coordsOfTarget[1] < Coords[1] + (self.winfo_height() / 4) <\
         coordsOfTarget[1] + target.winfo_height():
        collisionAction()

    elif coordsOfTarget[0] < Coords[0] + (self.winfo_width() / (4/3)) <\
         coordsOfTarget[0] + target.winfo_width() and\
         coordsOfTarget[1] < Coords[1] + (self.winfo_height() / (4/3)) <\
         coordsOfTarget[1] + target.winfo_height():
        collisionAction()