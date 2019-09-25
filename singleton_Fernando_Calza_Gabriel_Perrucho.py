class Placar:

    __instance = None
    placar = dict()

    @staticmethod
    def instance():
        if not Placar.__instance:
            Placar.__instance = Placar()
        return Placar.__instance

    def print_placar(self):
        for key, value in self.placar.items():
            print("nome " + key)

            for key2, value2 in value.items():
                print("placar " + str(key2))
                print("qtd " + str(value2))

    def adicionar_placar(self, nome, qtd, tipo):
        if nome in self.placar.keys():
            if tipo in self.placar[nome].keys():
                self.placar[nome][tipo] += qtd
            else:
                self.placar[nome][tipo] = qtd
        else:
            self.placar.update({nome: {tipo: qtd}})


placar = Placar.instance()


placar.adicionar_placar("Antonio", 4, "estrela")

placar.adicionar_placar("Antonio", 8, "estrela")

placar.adicionar_placar("Antonio", 6, "up")

placar2 = Placar.instance()

placar2.adicionar_placar("Antonio", 5, "estrela")

placar2.adicionar_placar("Antonio", 7, "like")

placar.print_placar()

print(" ")

print(" ")

placar2.print_placar()



