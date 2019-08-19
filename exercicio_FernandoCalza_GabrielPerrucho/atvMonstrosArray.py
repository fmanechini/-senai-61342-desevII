from random import randint
import json
import os

class Monstro:
    metodoAtaque = 0
    metodoDefesa = 0


    def __str__(self):  # sobrescreve o método str padrao pois o padrao retorna o endereco de memoria do objeto
        return self.nome

    def __init__(self, nome, tipo, poderAtaque, poderDefesa, pontoVida, grauEvo, nivel):
        self.nome = nome
        self.tipo = tipo
        self.poderAtaque = poderAtaque
        self.poderDefesa = poderDefesa
        self.pontoVida = pontoVida
        self.grauEvo = grauEvo
        self.nivel = nivel
        self.Defesas = []
        self.Ataques = []

    def MetodoAtq(self):
        self.Ataques.clear()
        for _ in range(10):
            self.Ataques.append(self.poderAtaque * self.grauEvo * self.nivel * randint(1, 5))

    def MetodoDef(self):
        self.Defesas.clear()
        for _ in range(10):
            self.Defesas.append(self.poderDefesa * self.grauEvo * self.nivel * randint(1, 3))
    
    def passarNivel(self):
        if self.tipo == "eletrico":
            self.pontoVida += 10
            self.poderDefesa += 1
            self.nivel += 1
            print(self.nome + " passou para o nivel " + str(self.nivel))
            print("O poder de Defesa aumentou de" + str(self.poderDefesa-1) + " para " + str(self.poderDefesa))
            print("Os pontos de vida aumentaram de " + str(self.pontoVida-10) + " para " + str(self.pontoVida))
        elif self.tipo == "fogo":
            self.poderAtaque += 1
            self.poderDefesa += 1
            self.nivel += 1
            print(self.nome + " passou para o nivel " + str(self.nivel))
            print("O poder de Defesa aumentou de " + str(self.poderDefesa-1) + " para " + str(self.poderDefesa))
            print("O poder de Ataque aumentou de " + str(self.poderAtaque-1) + " para " + str(self.poderAtaque))
        elif self.tipo == "agua":
            self.poderAtaque += 1
            self.pontoVida += 15
            self.nivel += 1
            print(self.nome + " passou para o nivel " + str(self.nivel))
            print("O poder de Ataque aumentou de " + str(self.poderAtaque-1) + " para " + str(self.poderAtaque))
            print("Os pontos de vida aumentaram de " + str(self.pontoVida-15) + " para " + str(self.pontoVida))
        else:
            self.pontoVida += 20
            self.nivel += 1
            print(self.nome + " passou para o nivel " + str(self.nivel))
            print("Os pontos de vida aumentaram de " + str(self.pontoVida-20) + " para " + str(self.pontoVida))

conteudo = open(os.path.dirname(__file__)+'/dadosMonstros.json').read()
listamonstros = json.loads(conteudo)
Competidores = []
for dadoMonstro in listamonstros:
    monstro = Monstro(dadoMonstro["nome"],dadoMonstro["tipo"],dadoMonstro["poderAtaque"],dadoMonstro["poderDefesa"],dadoMonstro["pontoVida"],dadoMonstro["grauEvo"],dadoMonstro["nivel"])
    Competidores.append(monstro)

def batalha(monstro1, monstro2):
    monstro1.MetodoAtq()
    monstro2.MetodoAtq()
    monstro1.MetodoDef()
    monstro2.MetodoDef()
    Danos1 = []
    Danos2 = []
    pv1 = monstro1.pontoVida
    pv2 = monstro2.pontoVida

    for numero in range(10):
        Danos1.append(monstro1.Ataques[numero] - monstro2.Defesas[numero])
        Danos2.append(monstro2.Ataques[numero] - monstro1.Defesas[numero])

    for numero in range(10):
        if pv1 > 0 or pv2 > 0:
            if Danos1[numero] > 0:
                pv2 = pv2 - Danos1[numero]
            if Danos2[numero] > 0:
                pv1 = pv1 - Danos2[numero]
    print("O " + monstro1.__str__() + " ficou com " + str(pv1) + " pontos de vida")
    print("O " + monstro2.__str__() + " ficou com " + str(pv2) + " pontos de vida")
    if pv1 > pv2:
        print(monstro1.__str__() + " ganhou")
        monstro1.passarNivel()
        return monstro1
    else:
        print(monstro2.__str__() + " ganhou")
        monstro2.passarNivel()
        return monstro2


def campeonato():
    quartasFinal = []
    semiFinal = []
    final = []

    for i in range(0, (len(Competidores) - 1), 2):
        m1, m2 = Competidores[i], Competidores [i + 1]
        quartasFinal.append(batalha(m1,m2))
    
    for i in range(0, (len(quartasFinal) - 1), 2):
        m1, m2 = quartasFinal[i], quartasFinal [i + 1]
        semiFinal.append(batalha(m1,m2))
    
    for i in range(0, (len(semiFinal) - 1), 2):
        m1, m2 = semiFinal[i], semiFinal [i + 1]
        final.append(batalha(m1,m2))
    
    for i in range(0, (len(final) - 1), 2):
        m1, m2 = final[i], final [i + 1]
        vencedor = batalha(m1,m2)
    print("O vencedor do campeonato foi: " + vencedor.__str__())


campeonato()
