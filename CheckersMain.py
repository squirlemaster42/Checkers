from tkinter import * # Import tkinter
    
class CanvasDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Canvas Demo") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 340, height = 340,
            bg = "white")
        self.canvas.pack()
        
        # Place buttons in frame
        frame = Frame(window)
        frame.pack()
        btMakeBoard = Button(frame, text = "Make Board", command = self.makeBoardPart1)
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

CanvasDemo() # Create GUI 
