class Like:

	def __init__(self):
		self.placar = dict()
		self.tipo = "like"
	
	def adicionar_placar(self, nome, qtd):
		if nome in self.placar.keys():
			self.placar[nome] += qtd
		else:
			self.placar.update({nome: qtd})
	
	def print_placar(self):
		print(self.tipo)
		print(self.placar)

class Estrela:

	def __init__(self):
		self.placar = dict()
		self.tipo = "estrela"

	def adicionar_placar(self, nome, qtd):
		if nome in self.placar.keys():
			self.placar[nome] += qtd
		else:
			self.placar.update({nome: qtd})
	
	def print_placar(self):
		print(self.tipo)
		print(self.placar)

class Up:

	def __init__(self):
		self.placar = dict()
		self.tipo = "up"

	def adicionar_placar(self, nome, qtd):
		if nome in self.placar.keys():
			self.placar[nome] += qtd
		else:
			self.placar.update({nome: qtd})
	
	def print_placar(self):
		print(self.tipo)
		print(self.placar)

class Factory:

	def build(self, tipo):
		if tipo == "estrela":
			return Estrela()
		elif tipo == "like":
			return Like()
		elif tipo == "up":
			return Up()
		else:
			print("Não trabalhamos dessa maneira")

factory = Factory()

pontos = factory.build("like")
pontos.adicionar_placar("joao", 5)
pontos.print_placar()

pontos.adicionar_placar("joao", 7)
pontos.print_placar()

pontos = factory.build("estrela")

pontos.adicionar_placar("joao", 10)
pontos.print_placar()

pontos.adicionar_placar("joao", 1)
pontos.print_placar()

pontos = factory.build("up")

pontos.adicionar_placar("joao", 4)
pontos.print_placar()

pontos = factory.build("coracoes")