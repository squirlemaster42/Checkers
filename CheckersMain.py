from tkinter import *
    
class CanvasDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Canvas Demo") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 340, height = 340,
            bg = "white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.processMouseEvent)

        # Place buttons in frame
        frame = Frame(window)
        frame.pack()
        btMakeBoard = Button(frame, text = "Reset Board", command = self.makeBoardPart1)
        btMakeBoard.grid(row = 1, column = 1)
        
        window.mainloop() # Create an event loop

    # Display a rectangle
    def makeBoardPart1(self):
        self.canvas.create_rectangle(10, 10, 330, 330, tags = "outline")
        y = 10
        x = 10
        while x < 320:
            while y < 320:
                self.canvas.create_rectangle(x, y, x + 40, y + 40, fill = "black", tags = "squares")
                y += 80
            y = 10
            x += 80
        self.makeBoardPart2()

    def makeBoardPart2(self):
        y = 50
        x = 50
        while x < 320:
            while y < 320:
                self.canvas.create_rectangle(x, y, x + 40, y + 40, fill = "black", tags = "squares")
                y += 80
            y = 50
            x += 80

    def setPieces(self):
        x1 = 10
        while x1 < 320:
            self.canvas.create_oval(x1, 10, x1 + 40, 50, fill = "red", tags = "red")
            x1 += 80

        x1 = 10
        while x1 < 320:
            self.canvas.create_oval(x1, 90, x1 + 40, 130, fill = "red", tags = "red")
            x1 += 80

        x1 = 50
        while x1 < 320:
            self.canvas.create_oval(x1, 50, x1 + 40, 90, fill = "red", tags = "red")
            x1 += 80

        x1 = 50
        while x1 < 320:
            self.canvas.create_oval(x1, 210, x1 + 40, 250, fill = "white", tags = "white")
            x1 += 80

        x1 = 50
        while x1 < 320:
            self.canvas.create_oval(x1, 290, x1 + 40, 330, fill = "white", tags = "white")
            x1 += 80

        x1 = 10
        while x1 < 320:
            self.canvas.create_oval(x1, 250, x1 + 40, 290, fill = "white", tags = "white")
            x1 += 80

    def processMouseEvent(self, event):
        print(event.x, event.y)
        print(event.x_root, event.y_root)
        print(event.num)

    def makeVirtualBoard(self):
        virtualBoard = [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
        ]
        return virtualBoard

CanvasDemo() # Create GUI 
