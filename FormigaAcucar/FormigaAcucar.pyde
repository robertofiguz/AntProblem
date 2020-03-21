def setup():
    size(1000,500) #cria um canvas de 1000x500 sendo que a matriz estara em apenas 500x500
    estrutura.desenharMatriz() #Cria a matriz
    formiga.comerAcucar()

def draw():
    formiga.moverFormiga() #metodo para movimentar a formiga

class Estrutura(): #class utilizada para definir a estrutura (matriz)
    Tmatriz = [4,4] #tamanho da matriz (x,y)
    cRect = 500/Tmatriz[0] #comprimento de cada espaço na matriz correspode ao tamanho dedicado a matriz a divir pelo numero de espaços na matriz
    aRect = 500/Tmatriz[1] #altura de cada espaço na matriz correspode ao tamanho dedicado a matriz a divir pelo numero de espaços na matriz
    def desenharMatriz(self):
        for y in range(self.Tmatriz[1]): #2 for loops para desenhar a matriz por
          for x in range(self.Tmatriz[0]):
              rect(x*Estrutura.cRect,y*Estrutura.aRect,Estrutura.cRect,Estrutura.aRect) #argumentos: coordenada X, coordenada Y, largura, altura

class Formiga:
    posicao = [floor((Estrutura.Tmatriz[0]-1)/2),floor((Estrutura.Tmatriz[1]-1)/2)]#posição da formiga iniciada no centro da matriz
    movimento = True
    movimentoNumero = 1
    setNumero  = 1

    def moverFormiga(self):
        for i in range(Estrutura.Tmatriz[0]):
            for i in range(self.setNumero):
                if(self.setNumero == min(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1])):
                    self.ultimoSet()
                self.direcao("L")
            for i in range(self.setNumero):
                self.direcao("V")
            self.setNumero  += 1

    def ultimoSet(self):
        if(Estrutura.Tmatriz[0] <= Estrutura.Tmatriz[1]):
            for i in range(self.setNumero-1):
                self.direcao("L")
        else:
            for i in range(self.setNumero):
                self.direcao("L")
            for i in range(self.setNumero-1):
                self.direcao("V")
        resultados.output(self.movimentoNumero)

    def direcao(self, mov):
        if(self.movimento):
            if(mov=="L"):
                if ((self.setNumero)%2):
                    self.posicao[0] += 1 #moves Right
                else:
                    self.posicao[0] -= 1 #moves Left
            if(mov=="V"):
                if ((self.setNumero)%2):
                    self.posicao[1] += 1 #moves Down
                else:
                    self.posicao[1] -= 1#moves Up
            self.movimentoNumero += 1
            self.comerAcucar()

    def calcularCentro(self):
        x =  self.posicao[0] * Estrutura.cRect # centro do retangulo corresponde ao indice do quadrado * comprimento do retangulo/altura
        y =  self.posicao[1] * Estrutura.aRect
        return [x,y] #retorno do centro sobre a forma de array

    def comerAcucar(self): #assinalar local onde a formiga já passou
        centro = self.calcularCentro()
        fill(120,120,120)
        rect(centro[0],centro[1], Estrutura.cRect, Estrutura.aRect)
        fill(255,255,255)
        fontSize = 30 + (-(max(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1])))
        textSize(fontSize)
        text(str(self.movimentoNumero),centro[0] + Estrutura.cRect/2 ,centro[1] +  Estrutura.aRect/2 )

class Resultados:
    def output(self,gramasAcucar):
        Formiga.movimento = False #define o movimento como falso, desta forma indicando que chegou ao fim do percurso
        gramasPorColetar = estrutura.Tmatriz[0]*estrutura.Tmatriz[1] - gramasAcucar #calculo das gramas de açucar que não foram apanhadas utilizando o numero total de retangulos e subtraindo o numero de apanhados
        outputMessage = "Gramas coletadas: " + str(gramasAcucar) + "\nGramas por coletar: " + str(gramasPorColetar) # mensagem de output
        textSize(20)
        text(str(outputMessage),600,100)

formiga = Formiga()
estrutura = Estrutura()
resultados = Resultados()
