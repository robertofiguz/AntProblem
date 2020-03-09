import time #importa biblioteca time para definir a velocidade da formiga
def setup():
    size(1000,500) #cria um canvas de 1000x500 sendo que a matriz estara em apenas 500x500
    estrutura.desenharMatriz() #Cria a matriz
def draw():
    if formiga.movimento: #verifica que não chegou ao final do percurso
        formiga.moverFormiga() #metodo para movimentar a formiga
class Estrutura(): #class utilizada para definir a estrutura (matriz)
    Tmatriz = [30,24] #tamanho da matriz (x,y)
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
    position = [floor(Tmatriz[0]/2),floor(Tmatriz[1]/2)]#posição da formiga iniciada no centro da matriz 
    movimento = True 
    gramasAcucar = 1 
    velocidade = 100/float(Tmatriz[0]*Tmatriz[1]) #a velocidade da formiga corresponde ao tamanho da matriz a dividir por uma constante, desta forma temos velocidade constante independentemente do tamanho da matriz
    rotacoes = 1 #numero de rotações consecutivas 
    
    def moverFormiga(self):
     #   time.sleep(self.velocidade) 
        if (self.checkEnd()): #verifica se se encontra num "final" - proximo quadrado já foi utilizado ou é inexistente 
            self.turnRight() #caso seja "final" formiga roda 90º para a direita
            self.rotacoes += 1
        else:
            self.comerAcucar()#funçao para tornar o quadrado cinzento
            self.position = self.getNextSquare() #Calculo da nova posição da formiga
            self.gramasAcucar +=1 #incremento do numero de gramas de açucar coletado
            self.rotacoes = 1 #redefiniçao do numero de rotaçoes pois a formiga já se movimentou 
        self.comerAcucar()
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
        
    def turnRight(self):
        if (self.rotacoes == 2): # se o numero de rotações consecutivas é igual a 2 a formiga terá chegado ao fim do percurso
            results.output(self.gramasAcucar) #metodo utilizado para fazer display dos resultados, passando o parametro gramasAcucar 
        elif( self.heading<3):
            self.heading += 1 #mudar a orientação incrementando o inice
        else:
            self.heading = 0 #reset do inice quando se encontra no ultimo indice
        self.corpo = reverse(self.corpo) #inverter as medidas do corpo da formiga (rotação de 90º)
            
    def checkHeading(self):
            headingArray = [ "N","E","S","W"] #array contendo orientações
            return headingArray[self.heading] 
        
    def getNextSquare(self): #função para calcular proximo movimento
            x =  self.position[0] 
            y = self.position[1]
            #tendo em conta qual a orientação da formiga podemos calcular qual a direção pretendida 
            if (self.checkHeading()=="N"):
                y -= 1
            elif(self.checkHeading() =="S"):
                y += 1
            elif(self.checkHeading()=="W"):
                x -= 1
            elif(self.checkHeading() =="E"):
                x += 1
            local = [x,y]
            return local
    def checkColour(self): #verifica a cor do proximo retangulo, desta forma evitando que esta passe por locais já utilizados
            xy = self.getNextSquare()
            x = (xy[0] *self.cRect) +self.cRect/2
            y = (xy[1] * self.aRect) + self.aRect/2
            c = get(x,y)
            if c != -1:
                return True
            
    def checkEnd(self): #verifica a combinação de cor e se a formiga se encontra no ultimo quadrado na sua orientação fazendo return de uma boolean
        if( self.checkColour() and   self.position[1] != 0 or self.checkHeading() == "N" and   self.position[1] == 0):
            return True
        elif( self.checkColour() and  self.Tmatriz[1]-1 != 0 or self.checkHeading() == "S" and   self.position[1] ==  self.Tmatriz[1]-1):
            return True
        elif( self.checkColour() and   self.position[0] != 0 or self.checkHeading() == "W" and   self.position[0] == 0):
            return True
        elif( self.checkColour() and  self.Tmatriz[0]-1 != 0 or self.checkHeading() == "E" and   self.position[0] ==  self.Tmatriz[0]-1):
            return True
        else:
            return False

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
