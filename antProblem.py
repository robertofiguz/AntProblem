#need to stop multiple turns without changing spot
arraySize = [10,10]
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
        self.body =[10,20]#w,h

    def turnRight(self):

        if((self.heading)<3):
            self.heading += 1
        else:
            self.heading = 0
        if (self.checkHeading() == "N" or self.checkHeading() == "S"):
            self.body = 10,20
        else:
            self.body = 20,10

    def checkColour(self,x,y):
        self.x1 = (x *50) +25
        self.y1 = (y * 50) +25
        c = get(self.x1, self.y1)
        if c != -1:
            return True
    def checkHeading(self):
        return self.headingArray[self.heading]

    def checkEnd(self):
            if(self.checkHeading() == "N" and  self.checkColour(self.position[0],self.position[1] - 1) and self.position[1] != 0):
                return True
            elif(self.checkHeading() == "S" and  self.checkColour(self.position[0],self.position[1] + 1) and self.arraySize[1]-1 != 0):
                return True
            elif(self.checkHeading() == "W" and  self.checkColour(self.position[0]-1,self.position[1]) and self.position[0] != 0):
                return True
            elif(self.checkHeading() == "E" and  self.checkColour(self.position[0]+1,self.position[1]) and self.arraySize[0]-1 != 0):
                return True
            elif(self.checkHeading() == "N" and self.position[1] == 0 ):
                return True
            elif(self.checkHeading() == "S" and self.position[1] == self.arraySize[0]-1):
                return True
            elif(self.checkHeading() == "W" and self.position[0] == 0 ):
                return True
            elif(self.checkHeading() == "E" and self.position[0] == self.arraySize[1]-1):
                return True
            else:
                return False
    def blackSquare(self):
        x = self.position[0] *50
        y = self.position[1] * 50
        fill(40,40,40)
        rect(x,y,50,50)
    def getNextSquare(self):
        localPosition = self.position
        print(localPosition)
        if (self.checkHeading()=="N"):
            localPosition[1] =  self.position[1] - 1
        if(self.checkHeading() =="S"):
            localPosition[1] =self.position[1] + 1
        if (self.checkHeading()=="W"):
            localPosition[0] =self.position[0] - 1
        if(self.checkHeading() =="E"):
            localPosition[0] = self.position[0] + 1
        print(localPosition)
        return localPosition
    def movimentar(self):
     #   print(self.heading)
       # time.sleep(0.5
        if (self.checkEnd()):
            self.turnRight()
            print(self.position)
        else:
            self.blackSquare()
            self.position = self.getNextSquare()
        self.blackSquare()
        fill(0)
        ellipse((self.position[0] * 50)+25, (self.position[1]*50)+25, self.body[1], self.body[0])

Formiga = formiga(position=[ floor(arraySize[1]/2),floor(arraySize[0]/2)], arraySize = arraySize)
