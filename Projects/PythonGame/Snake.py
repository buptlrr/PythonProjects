from Tkinter import *
import random
class snake(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.body = [(0,0)]
                self.bodyid = []
                self.food = [ -1, -1 ]
                self.foodid = -1
                self.gridcount = 10 
                self.size = 500
                self.di = 3
                self.speed = 500

                self.top = self.winfo_toplevel()
                self.top.resizable(False, False)
                self.grid()
                self.canvas = Canvas(self)
                self.canvas.grid()
                self.canvas.config(width=self.size, height=self.size,relief=RIDGE)

                self.drawgrid()
                s = self.size/self.gridcount
                id = self.canvas.create_rectangle(self.body[0][0]*s,self.body[0][1]*s, 
                        (self.body[0][0]+1)*s, (self.body[0][1]+1)*s, fill="yellow")
                self.bodyid.insert(0, id)
                self.bind_all("<KeyRelease>", self.keyrelease)
                self.drawfood()
                self.after(self.speed, self.drawsnake)
        def drawgrid(self):
                s = self.size/self.gridcount
                for i in range(0, self.gridcount+1):
                        self.canvas.create_line(i*s, 0, i*s, self.size)
                        self.canvas.create_line(0, i*s, self.size, i*s)
        def drawsnake(self):
                s = self.size/self.gridcount
                head = self.body[0]
                new = [head[0], head[1]] 
                if self.di == 1:
                        new[1] = (head[1]-1) % self.gridcount
                elif self.di == 2:
                        new[0] = (head[0]+1) % self.gridcount
                elif self.di == 3:
                        new[1] = (head[1]+1) % self.gridcount
                else:
                        new[0] = (head[0]-1) % self.gridcount
                next = ( new[0], new[1] )
                if next in self.body:
                        exit()
                elif next == (self.food[0], self.food[1]):
                        self.body.insert(0, next)
                        self.bodyid.insert(0, self.foodid)
                        self.drawfood()
                else:
                        tail = self.body.pop()
                        id = self.bodyid.pop()
                        self.canvas.move(id, (next[0]-tail[0])*s, (next[1]-tail[1])*s)
                        self.body.insert(0, next)
                        self.bodyid.insert(0, id)

                self.after(self.speed, self.drawsnake)
        def drawfood(self):
                s = self.size/self.gridcount
                x = random.randrange(0, self.gridcount)
                y = random.randrange(0, self.gridcount)
                while (x, y) in self.body:
                        x = random.randrange(0, self.gridcount)
                        y = random.randrange(0, self.gridcount)
                id = self.canvas.create_rectangle(x*s,y*s, (x+1)*s, (y+1)*s, fill="yellow")
                self.food[0] = x
                self.food[1] = y
                self.foodid = id
        def keyrelease(self, event):
                if event.keysym == "Up" and self.di != 3:
                        self.di = 1
                elif event.keysym == "Right" and self.di !=4:
                        self.di = 2
                elif event.keysym == "Down" and self.di != 1:
                        self.di = 3
                elif event.keysym == "Left" and self.di != 2:
                        self.di = 4

app = snake()
app.master.title("Greedy Snake")
app.mainloop()