#need to stop multiple turns without changing spot
arraySize = [40,40]
import time
def setup():
    for a in range(arraySize[0]):
        for i in range(arraySize[1]):
            rect(i*50,a*50,50,50)
    size(arraySize[1]*50,arraySize[0]*50)


def draw():
    setupFormiga()

def setupFormiga():
    Formiga.movimentar()

class formiga:
    def __init__(self, position, arraySize):
        self.arraySize = arraySize
        self.position = position
        self.heading = 0
        self.headingArray = ["N","E","S","W"]
        self.w = 10
        self.h = 20

    def turnRight(self):

        if((self.heading)<3):
            self.heading += 1
        else:
            self.heading = 0
        if (self.headingArray[self.heading] == "N" or self.headingArray[self.heading] == "S"):
            self.w = 10
            self.h = 20
        else:
            self.w = 20
            self.h = 10

    def checkColour(self,x,y):
        self.x1 = (x *50) +25
        self.y1 = (y * 50) +25
        c = get(self.x1, self.y1)
        if c != -1:
            return True

    def checkEnd(self):
        if(self.headingArray[self.heading] == "N" and  self.checkColour(self.position[0],self.position[1] - 1) and self.position[1] != 0):
            return True
        elif(self.headingArray[self.heading] == "S" and  self.checkColour(self.position[0],self.position[1] + 1) and self.arraySize[1]-1 != 0):
            return True
        elif(self.headingArray[self.heading] == "W" and  self.checkColour(self.position[0]-1,self.position[1]) and self.position[0] != 0):
            return True
        elif(self.headingArray[self.heading] == "E" and  self.checkColour(self.position[0]+1,self.position[1]) and self.arraySize[0]-1 != 0):
            return True
        elif(self.headingArray[self.heading] == "N" and self.position[1] == 0 ):
            return True
        elif(self.headingArray[self.heading] == "S" and self.position[1] == self.arraySize[0]-1):
            return True
        elif(self.headingArray[self.heading] == "W" and self.position[0] == 0 ):
            return True
        elif(self.headingArray[self.heading] == "E" and self.position[0] == self.arraySize[1]-1):
            return True
        else:
            return False
    def blackSquare(self):
        x = self.position[0] *50
        y = self.position[1] * 50
        fill(40,40,40)
        rect(x,y,50,50)

    def movimentar(self):
        print(self.position)
       # time.sleep(0.5)
        self.blackSquare()
        if (self.checkEnd()):
            self.turnRight()

        else:
            if (self.headingArray[self.heading]=="N"):
                self.position[1] -= 1

            if(self.headingArray[self.heading] =="S"):
                self.position[1] += 1

            if (self.headingArray[self.heading]=="W"):
                self.position[0] -= 1

            if(self.headingArray[self.heading] =="E"):
                self.position[0] += 1

        fill(0)
        ellipse((self.position[0] * 50)+25, (self.position[1]*50)+25, self.w, self.h)

Formiga = formiga(position=[ floor(arraySize[1]/2),floor(arraySize[0]/2)], arraySize = arraySize)
