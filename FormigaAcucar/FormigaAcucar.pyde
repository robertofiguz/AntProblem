import time #importa biblioteca time para definir a velocidade da formiga
def setup():
    size(1000,500) #cria um canvas de 1000x500 sendo que a matriz estara em apenas 500x500
    estrutura.desenharMatriz() #Cria a matriz
    formiga.comerAcucar()
def draw():
    formiga.moverFormiga() #metodo para movimentar a formiga

class Estrutura(): #class utilizada para definir a estrutura (matriz)
    Tmatriz = [5,20] #tamanho da matriz (x,y)
    comprimentoRect = 500/Tmatriz[0] #comprimento de cada espaço na matriz correspode ao tamanho dedicado a matriz a divir pelo numero de espaços na matriz
    alturaRect = 500/Tmatriz[1] #altura de cada espaço na matriz correspode ao tamanho dedicado a matriz a divir pelo numero de espaços na matriz
    def desenharMatriz(self):
        for y in range(self.Tmatriz[1]): #2 for loops para desenhar a matriz por
          for x in range(self.Tmatriz[0]):
              rect(x*self.comprimentoRect,y*self.alturaRect,self.comprimentoRect,self.alturaRect) #argumentos: coordenada X, coordenada Y, largura, altura

class Formiga:
    cRect = Estrutura.comprimentoRect
    aRect = Estrutura.alturaRect
    position = [floor((Tmatriz[0]-1)/2),floor((Tmatriz[1]-1)/2)]#posição da formiga iniciada no centro da matriz
    movimento = True
    moveNumber = 1
    currentSet  = 1

    def moverFormiga(self):
        for i in range(Estrutura.Tmatriz[0]):
            for i in range(self.currentSet):
                if(self.currentSet == min(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1])):
                    self.lastSet()
                self.direcao("L")
            for i in range(self.currentSet):
                self.direcao("V")
            self.currentSet  += 1

    def lastSet(self):
        if(Estrutura.Tmatriz[0] <= Estrutura.Tmatriz[1]):
            for i in range(self.currentSet-1):
                self.direcao("L")
        else:
            for i in range(self.currentSet):
                self.direcao("L")
            for i in range(self.currentSet-1):
                self.direcao("V")
        results.output(self.moveNumber)

    def direcao(self, direction):
        if(self.movimento):
            if(direction=="L"):
                if ((self.currentSet)%2):
                    self.position[0] += 1 #moves Right
                else:
                    self.position[0] -= 1 #moves Left
            if(direction=="V"):
                if ((self.currentSet)%2):
                    self.position[1] += 1 #moves Down
                else:
                    self.position[1] -= 1#moves Up
            self.moveNumber += 1
            self.comerAcucar()

    def calcularCentro(self):
        x =  self.position[0] * self.cRect # centro do retangulo corresponde ao indice do quadrado * comprimento do retangulo/altura
        y =  self.position[1] * self.aRect
        return [x,y] #retorno do centro sobre a forma de array

    def comerAcucar(self): #assinalar local onde a formiga já passou
        centro = self.calcularCentro()
        fill(120,120,120)
        rect(centro[0],centro[1], self.cRect, self.aRect)
        fill(255,255,255)
        fontSize = 10 + (-(max(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1])))+20
        textSize(fontSize)
        text(str(self.moveNumber),centro[0] + self.cRect/2 ,centro[1] +  self.aRect/2 )

class Results:
    def output(self,gramasAcucar):
        Formiga.movimento = False #define o movimento como falso, desta forma indicando que chegou ao fim do percurso
        gramasPorColetar = estrutura.Tmatriz[0]*estrutura.Tmatriz[1] - gramasAcucar #calculo das gramas de açucar que não foram apanhadas utilizando o numero total de retangulos e subtraindo o numero de apanhados
        outputMessage = "Gramas coletadas: " + str(gramasAcucar) + "\nGramas por coletar: " + str(gramasPorColetar) # mensagem de output
        textSize(20)
        text(str(outputMessage),600,100)

formiga = Formiga()
estrutura = Estrutura()
results = Results()
