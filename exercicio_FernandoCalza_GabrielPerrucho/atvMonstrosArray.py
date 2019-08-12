from random import randint
class Monstro:
    metodoAtaque = 0
    metodoDefesa = 0
    Defesas = []
    Ataques = []



    def __str__(self): #sobrescreve o método str padrao pois o padrao retorna o endereco de memoria do objeto
        return self.nome

    def __init__(self,nome,tipo, poderAtaque, poderDefesa, pontoVida, grauEvo, nivel):
        self.nome = nome
        self.tipo = tipo
        self.poderAtaque = poderAtaque
        self.poderDefesa = poderDefesa
        self.pontoVida = pontoVida
        self.grauEvo = grauEvo
        self.nivel = nivel

    def MetodoAtq(self):
        self.Ataques.clear()
        for _ in range(10):
            self.Ataques.append(self.poderAtaque * self.grauEvo * self.nivel * randint(1, 5))
            
        
    
    
    def MetodoDef(self):
        self.Defesas.clear()
        for _ in range(10):
            self.Defesas.append(self.poderDefesa * self.grauEvo * self.nivel * randint(1, 3))

pikachu = Monstro("pikachu", "eletrico", 3, 2, 300, 1, 5)
charmander = Monstro("charmander", "fogo", 3, 3, 250, 1, 5)
acqua = Monstro("acqua", "agua", 3, 1, 260, 1, 5)
fluff = Monstro("fluff", "terra", 2, 3, 240, 1, 5)
haleluia = Monstro("haleluia", "holy", 2, 2, 300, 1, 5)
lilith = Monstro("lilith", "dark", 3, 3, 250, 1, 5)
aerea = Monstro("aerea", "ar", 3, 2, 260, 1, 5)
metal = Monstro("metal", "metal", 1, 2, 240, 1, 5)
Competidores = [pikachu,charmander,acqua,fluff,haleluia,lilith,aerea,metal]

def batalha(monstro1,monstro2):
    monstro1.MetodoAtq()
    monstro2.MetodoAtq()
    monstro1.MetodoDef()
    monstro2.MetodoDef()
    Danos1 = []
    Danos2 = []
    print(monstro1.Ataques)
    print(monstro1.Defesas)
    print(monstro2.Ataques)
    print(monstro2.Defesas)
    
    for numero in range(10):
        Danos1.append(monstro1.Ataques[numero] - monstro2.Defesas[numero])
        Danos2.append(monstro2.Ataques[numero] - monstro1.Defesas[numero])
        

    for numero in range(10):
        if Danos1[numero] > 0:
            monstro1.pontoVida = monstro1.pontoVida - Danos1[numero]
        if Danos2[numero] > 0:
            monstro2.pontoVida = monstro2.pontoVida - Danos2[numero]
    print("O " + monstro1.__str__() + " ficou com " + str(monstro1.pontoVida) + " pontos de vida")
    print("O " + monstro2.__str__() + " ficou com " + str(monstro2.pontoVida) + " pontos de vida")
    if monstro1.pontoVida > monstro2.pontoVida:
        print(monstro1.__str__() + " ganhou")
        return monstro1
    else:
        print(monstro2.__str__() + " ganhou")
        return monstro2

def campeonato():
    semifinal = []
    final = []
    semifinal.append(batalha(Competidores[0],Competidores[1]))
    semifinal.append(batalha(Competidores[2],Competidores[3]))
    semifinal.append(batalha(Competidores[4],Competidores[5]))
    semifinal.append(batalha(Competidores[6],Competidores[7]))

    final.append(batalha(semifinal[0], semifinal[1]))
    final.append(batalha(semifinal[2], semifinal[3]))
    
    vencedor = batalha(final[0], final[1])
    print("O vencedor do campeonato foi: " + vencedor.__str__())


campeonato()