def setup():
    size(1000,500) #cria um canvas de 1000x500 sendo que a matriz estara em apenas 500x500
    estrutura.desenharMatriz() #Cria a matriz
    formiga.comerAcucar()#come o primeiro quadrado de açucar

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
    movimento = True #variavel utilizada para parar movimento da formiga
    movimentoNumero = 1 #variavel acumula numero de movimentos feitos pela formiga
    setNumero  = 1 #variavel guarda o set de movimentos em que se encontra

    def moverFormiga(self):#metodo utilizado para movimentar a formiga
            for i in range(self.setNumero):#numero de movimentos(verticais e horizontais) em cada set é igual ao numero de sets, ex: set nº2, 2 movimentos horizontais e 2 verticais, com exceção do ultimo set
                if(self.setNumero == min(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1])): #verificar se se encontra no ultimo set, o numero de sets é igual ao lado menor da matriz
                    self.ultimoSet() #iniciar metodo para executar ultimo set, definido separadamente para facilitar manutenção
                self.direcao("H") #movimentar na horizontal
            for i in range(self.setNumero):
                self.direcao("V")#movimentar na vertical
            self.setNumero  += 1#passar para proximo set

    def ultimoSet(self):
        if(Estrutura.Tmatriz[0] <= Estrutura.Tmatriz[1]): #no ultimo set o numero de movimentos é dependente do ratio da matriz
            for i in range(self.setNumero-1): #no ultimo set, caso o numero de espaços hotizontais seja inferior ou igual ao numero de espaços verticais, apenas são executados movimentos laterais
                self.direcao("H")#
        else:#caso o numero de espaços hotizontais seja superior, no ultimo set executam se movimentos horizontais e verticais, sendo o nº de movimentos verticais inferior em 1 unidade aos movimentos horizontais
            for i in range(self.setNumero):
                self.direcao("H")
            for i in range(self.setNumero-1):
                self.direcao("V")
        resultados.output(self.movimentoNumero)

    def direcao(self, mov): #define se o moviemnto horizontal ou vertical é para a esquerda, direita, para cima ou para baixo
        if(self.movimento):
            if(mov=="H"):
                if ((self.setNumero)%2):
                    self.posicao[0] += 1 #mover Direita
                else:
                    self.posicao[0] -= 1 #movet Esquerda
            if(mov=="V"):
                if ((self.setNumero)%2):
                    self.posicao[1] += 1 #mover Baixo
                else:
                    self.posicao[1] -= 1#mover Cima
            self.movimentoNumero += 1 #numero de movimentos incrementado
            self.comerAcucar()#chama o metodo para "comer o quadrado de açucar", colorindo e indicando o numero do movimento

    def calcularCentro(self):
        x =  self.posicao[0] * Estrutura.cRect # centro do retangulo corresponde ao indice do quadrado * comprimento do retangulo/altura
        y =  self.posicao[1] * Estrutura.aRect
        return [x,y] #retorno do centro sobre a forma de array

    def comerAcucar(self): #assinalar local onde a formiga já passou
        centro = self.calcularCentro() #calcular o centro do quadrado
        fill(120,120,120)#definir a cor para cinzemto
        rect(centro[0],centro[1], Estrutura.cRect, Estrutura.aRect)#colorir o quadrado
        fill(255,255,255)#definir a cor das letras para branco
        fontSize = 30 + (-(max(Estrutura.Tmatriz[0],Estrutura.Tmatriz[1]))) #definir o tamanho da fonte para ser inversamente proporcional ao tamanho das celulas da matriz
        textSize(fontSize)
        text(str(self.movimentoNumero),centro[0] + Estrutura.cRect/2 ,centro[1] +  Estrutura.aRect/2 )#escreve o numero do movimento na celula

class Resultados:
    def output(self,gramasAcucar):
        Formiga.movimento = False #define o movimento como falso, desta forma indicando que chegou ao fim do percurso
        gramasPorColetar = estrutura.Tmatriz[0]*estrutura.Tmatriz[1] - gramasAcucar #calculo das gramas de açucar que não foram apanhadas utilizando o numero total de retangulos e subtraindo o numero de apanhados
        outputMessage = "Gramas coletadas: " + str(gramasAcucar) + "\nGramas por coletar: " + str(gramasPorColetar) # mensagem de output
        textSize(20) #set the results text size to 20
        text(str(outputMessage),600,100)

formiga = Formiga()
estrutura = Estrutura()
resultados = Resultados()
