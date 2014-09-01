__author__ = 'Liew'

from Tkinter import *
import uuid
from PIL import Image, ImageDraw, ImageFont

class App:
    def __init__(self, root):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.green = (0,128,0)
        self.width = 450
        self.height = 450
        try:
            self.font = ImageFont.truetype("Arial.ttf", 12)
        except IOError as e:
            print e
            self.font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 12)
        self.canvaswidth = 400.0
        self.canvasheight = 150
        self.interval = 22
        self.time = 22
        self.linesecond = self.canvaswidth * 1/self.interval

        self.canvas = Canvas(root, width=self.canvaswidth, height=self.canvasheight, bg='white')
        self.image = Image.new("RGB", (int(self.canvaswidth), self.canvasheight), self.white)
        self.draw = ImageDraw.Draw(self.image)

        self.x1, self.y1, self.x2, self.y2 = 28, 50, 28, 50

        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='green')
        self.draw.line((self.x1, self.y1, self.x2, self.y2), self.green)

        self.canvas.create_line(28, 0, 28, 500)
        self.draw.line((28, 0, 28, 500), self.black)

        self.canvas.create_line(0, 110, self.canvaswidth, 110)
        self.draw.line((0, 110, self.canvaswidth, 110), self.black)

        canvas_id = self.canvas.create_text(3, 40, anchor="nw")
        self.canvas.insert(canvas_id, 50, "ON")
        self.draw.text((3, 40), "ON", font=self.font, fill=self.black)

        canvas_id2 = self.canvas.create_text(3, 90, anchor="nw")
        self.canvas.insert(canvas_id2, 90, "OFF")
        self.draw.text((3, 90), "OFF", font=self.font, fill=self.black)

        self.tick(self.time, int(self.interval))
        self.dingdong = 0

        # filename = "./images/" + str(uuid.uuid4()) + ".jpg"
        # self.image.save(filename)

        # self.canvas.bind('<Button-1>', lambda event, sec=self.linesecond: self.line1(event, sec))
        # self.canvas.bind('<Button-2>', lambda event, sec=self.linesecond: self.line1(event))
        # self.canvas.bind('<Button-3>', lambda event, sec=self.linesecond: self.line2(event, sec))


    def redraw(self):
        filename = str(uuid.uuid4()) + ".jpg"
        self.image.save("./static/" + filename)
        self.draw = None
        self.image = None
        self.image = Image.new("RGB", (int(self.canvaswidth), self.canvasheight), self.white)
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.delete("all")

        self.x1, self.y1, self.x2, self.y2 = 28, 50, 28, 50
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='green')
        self.draw.line((self.x1, self.y1, self.x2, self.y2), self.green)

        self.canvas.create_line(28, 0, 28, 500)
        self.draw.line((28, 0, 28, 500), self.black)

        self.canvas.create_line(0, 110, self.canvaswidth, 110)
        self.draw.line((28, 110, self.canvaswidth, 110), self.black)

        canvas_id = self.canvas.create_text(3, 40, anchor="nw")
        self.canvas.insert(canvas_id, 50, "ON")
        self.draw.text((3, 40), "ON", font=self.font, fill=self.black)

        canvas_id2 = self.canvas.create_text(3, 90, anchor="nw")
        self.canvas.insert(canvas_id2, 90, "OFF")
        self.draw.text((3, 90), "OFF", font=self.font, fill=self.black)
        #self.canvas.bind('<Button-1>', lambda event, sec=self.linesecond: self.line1(event, sec))
        #self.canvas.bind('<Button-3>', lambda event, sec=self.linesecond: self.line2(event, sec))
        self.tick(self.time, int(self.interval))

        self.dingdong = 0
        return filename

    def tik(self, status):
        self.dingdong += 1
        if status == "ON" and self.dingdong < 20:
            self.line1(self.linesecond)
        elif status == "OFF" and self.dingdong <20:
            self.line2(self.linesecond)
        else:
            return "end"

    def line1(self, second):
        #self.canvas.delete("all")

        if self.y2 == 50:
            self.x1, self.y1 = self.x2, self.y2
            self.x2 += second
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='green')
            self.draw.line((self.x1, self.y1, self.x2, self.y2), self.green)
            #print self.x2
        else:
            self.x1, self.y1 = self.x2, self.y2
            self.y2 = 50
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='green')
            self.draw.line((self.x1, self.y1, self.x2, self.y2), self.green)

            self.x1, self.y1 = self.x2, self.y2
            self.x2 += second
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='green')
            self.draw.line((self.x1, self.y1, self.x2, self.y2), self.green)

            #print self.x2

    def line2(self, second):
       # self.canvas.delete("all")
        if self.y2 == 0:
            self.x1, self.y1 = self.x2, self.y2
            self.x2 += second
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='red')
            self.draw.line((self.x1, self.y1, self.x2, self.y2), self.red)
            #print self.x2
        else:
            self.x1, self.y1 = self.x2, self.y2
            self.y2 = 100
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='red')
            self.draw.line((self.x1, self.y1, self.x2, self.y2), self.red)
            self.x1, self.y1 = self.x2, self.y2
            self.x2 += second
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='red')
            self.draw.line((self.x1, self.y1, self.x2, self.y2), self.red)
            #print self.x2

    def tick(self, time, interval=5):
        for x in range(0, interval):
            displaytime = time * x/interval
            self.linetime = self.canvaswidth * x/interval + 28
            #print self.linetime
            self.canvas.create_line(self.linetime, 115, self.linetime, 105)
            self.draw.line((self.linetime, 115, self.linetime, 105), self.black)

            canvas_id = self.canvas.create_text(self.linetime - 3, 120, anchor="nw")
            self.canvas.insert(canvas_id, 50, displaytime)
            self.draw.text((self.linetime - 3, 120), str(displaytime), font=self.font, fill=self.black)


    def grid(self, row=0, column=0):
        self.canvas.grid(row=row, column=column)

# root = Tk()
# root.wm_title("Denial Of Service Attack and Reporting Tool")
# app = App(root)
# root.mainloop()
