import time #importa biblioteca time para definir a velocidade da formiga

def setup():
    size(1000,500) #cria um canvas de 1000x500 sendo que a matriz estara em apenas 500x500
    estrutura.desenharMatriz() #Cria a matriz
def draw():
    if formiga.movimento: #verifica que não chegou ao final do percurso
        print(formiga.movimento)
        formiga.moverFormiga() #metodo para movimentar a formiga
     #  print(formiga.position)
class Estrutura(): #class utilizada para definir a estrutura (matriz)
    Tmatriz = [3,7] #tamanho da matriz (x,y)
    comprimentoRect = 500/Tmatriz[0] #comprimento de cada espaço na matriz correspode ao tamanho dedicado a matriz a divir pelo numero de espaços na matriz
    alturaRect = 500/Tmatriz[1] #altura de cada espaço na matriz correspode ao tamanho dedicado a matriz a divir pelo numero de espaços na matriz
    def desenharMatriz(self):
        for y in range(self.Tmatriz[1]): #2 for loops para desenhar a matriz por
          for x in range(self.Tmatriz[0]):
              rect(x*self.comprimentoRect,y*self.alturaRect,self.comprimentoRect,self.alturaRect) #argumentos: coordenada X, coordenada Y, largura, altura

class Formiga:
    Tmatriz = Estrutura.Tmatriz
    cRect = Estrutura.comprimentoRect
    aRect = Estrutura.alturaRect
    corpo = [cRect/2, aRect*0.8] # tamanho da formiga é metade da largura do quadrado e 80% do comprimento
    heading = 0 #orientação da formiga
    position = [floor((Tmatriz[0]-1)/2),floor((Tmatriz[1]-1)/2)]#posição da formiga iniciada no centro da matriz
    print(position)
    movimento = True
    gramasDeAcucar = 1
    move = 0
    currentSet  = 1
   # velocidade = 200/float(Tmatriz[0]*Tmatriz[1]) #a velocidade da formiga corresponde ao tamanho da matriz a dividir por uma constante, desta forma temos velocidade constante independentemente do tamanho da matriz


    def moverFormiga(self):
            for i in range(Estrutura.Tmatriz[0]):
               # for b in range(2):
                    for a in range(self.currentSet):
                        if(self.currentSet == min(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1]) and self.movimento):
                            #iniciar last Set
                            if(Estrutura.Tmatriz[0] <= Estrutura.Tmatriz[1]):
                                for a in range(self.currentSet-1):
                                    if ((self.currentSet )%2):
                                        self.moveR()
                                        print(self.position)
                                    else:
                                        self.moveL()
                                        print(self.position)
                            else:
                                for a in range(self.currentSet):
                                    if ((self.currentSet )%2):
                                        self.moveR()
                                        print(self.position)
                                    else:
                                        self.moveL()
                                        print(self.position)

                                for a in range(self.currentSet-1):
                                    if ((self.currentSet )%2):
                                        self.moveD()
                                        print(self.position)
                                    else:
                                        self.moveU()
                                        print(self.position)

                            print("Done")
                            results.output(1)
                            self.movimento = False
                            results.output(1)

                        elif ((self.currentSet )%2 and self.movimento):
                            self.moveR()
                            print(self.position)
                        elif(self.movimento):
                            self.moveL()
                            print(self.position)
                    for a in range(self.currentSet):
                        if ((self.currentSet)%2 and self.movimento):
                            self.moveD()
                            print(self.position and self.movimento)
                        elif (self.movimento):
                            self.moveU()
                            print(self.position)
                    self.currentSet  += 1
    def moveU(self):
        self.move += 1
        self.comerAcucar()
        self.position[1] -= 1
        self.desenharFormiga()
    def moveD(self):
        self.move += 1
        self.comerAcucar()
        self.position[1] += 1
        self.desenharFormiga()
    def moveL(self):
        self.move += 1
        self.comerAcucar()
        self.position[0] -= 1
        self.desenharFormiga()
    def moveR(self):
        self.move += 1
        self.comerAcucar()
        self.position[0] += 1
        self.desenharFormiga()


    def desenharFormiga(self):

        centro = self.calcularCentro()#calculo do centro do retangulo onde a formiga se encontra na matriz

        fill(0)
        ellipse(centro[0] + self.cRect/2, centro[1] +  self.aRect/2,  self.corpo[0],  self.corpo[1]) # desenho da formiga - argumentos: x, y, largura, altura


    def calcularCentro(self):
        x =  self.position[0] *self.cRect # centro do retangulo corresponde ao indice do quadrado * comprimento do retangulo/altura
        y =  self.position[1] *  self.aRect
        xy =[x,y]
        return xy #retorno do centro sobre a forma de array

    def comerAcucar(self): #assinalar local onde a formiga já passou
        centro = self.calcularCentro()
        fill(120,120,120)
        rect(centro[0],centro[1], self.cRect, self.aRect)
        fill(255,255,255)
        textSize(20)
        text(str(self.move),centro[0] + self.cRect/2,centro[1] +  self.aRect/2)


    def turnRight(self):
        #if (self.rotacoes == 5): # se o numero de rotações consecutivas é igual a 2 a formiga terá chegado ao fim do percurso
         #   results.output(self.gramasAcucar) #metodo utilizado para fazer display dos resultados, passando o parametro gramasAcucar
        if( self.heading<3):
            self.heading += 1 #mudar a orientação incrementando o inice
        else:
            self.heading = 0 #reset do inice quando se encontra no ultimo indice
        self.corpo = reverse(self.corpo) #inverter as medidas do corpo da formiga (rotação de 90º)


class Results:
    def output(self,gramasAcucar):
        Formiga.movimento = False #define o movimento como falso, desta forma indicando que chegou ao fim do percurso
        self.gramasAcucar = gramasAcucar
        gramasPorColetar = estrutura.Tmatriz[0]*estrutura.Tmatriz[1] - self.gramasAcucar #calculo das gramas de açucar que não foram apanhadas utilizando o numero total de retangulos e subtraindo o numero de apanhados
        outputMessage = "Gramas coletadas: " + str(self.gramasAcucar) + "\nGramas por coletar: " + str(gramasPorColetar) # mensagem de output
        textSize(20)
        text(str(outputMessage),600,100)

formiga = Formiga()
estrutura = Estrutura()
results = Results()
