from abc import ABC, abstractmethod


class AbstractMassasFactory(ABC):

    @abstractmethod
    def criar_massa(self):
        pass

    @abstractmethod
    def criar_ingrediente(self):
        pass


class FusilliBranco(AbstractMassasFactory):

    def criar_massa(self):
        return Fusilli()

    def criar_ingrediente(self):
        return Molho_branco()


class FusilliBacon(AbstractMassasFactory):

    def criar_massa(self):
        return Fusilli()

    def criar_ingrediente(self):
        return Bacon()

class FusilliVermelho(AbstractMassasFactory):

    def criar_massa(self):
        return Fusilli()

    def criar_ingrediente(self):
        return Molho_vermelho()

class FusilliMilho(AbstractMassasFactory):

    def criar_massa(self):
        return Fusilli()

    def criar_ingrediente(self):
        return Milho()

class EspagueteBranco(AbstractMassasFactory):

    def criar_massa(self):
        return Espaguete()

    def criar_ingrediente(self):
        return Molho_branco()

class EspagueteBacon(AbstractMassasFactory):

    def criar_massa(self):
        return Espaguete()

    def criar_ingrediente(self):
        return Bacon()

class EspagueteVermelho(AbstractMassasFactory):

    def criar_massa(self):
        return Espaguete()

    def criar_ingrediente(self):
        return Molho_vermelho()

class EspagueteMilho(AbstractMassasFactory):

    def criar_massa(self):
        return Espaguete()

    def criar_ingrediente(self):
        return Milho()

class AbstractMassa(ABC):

    @abstractmethod
    def dados_massa(self):
        pass


class Espaguete(AbstractMassa):
    def dados_massa(self):
        self.nome = "Espaguete"
        self.valor = 1.80


class Fusilli(AbstractMassa):
    def dados_massa(self):
        self.nome = "Fusilli"
        self.valor = 2.50

class AbstractIngrediente(ABC):

    @abstractmethod
    def dados_ingrediente(self):
        pass		

class Molho_vermelho(AbstractIngrediente):
    def dados_ingrediente(self):
        self.nome = "Molho Vermelho"
        self.valor = 4.00

class Molho_branco(AbstractIngrediente):
    def dados_ingrediente(self):
        self.nome = "Molho Branco"
        self.valor = 3.00

class Bacon(AbstractIngrediente):
    def dados_ingrediente(self):
        self.nome = "Bacon"
        self.valor = 2.00

class Milho(AbstractIngrediente):
    def dados_ingrediente(self):
        self.nome = "Milho"
        self.valor = 1.00

def client_code(factory):
    product_a = factory.criar_massa()
    product_a.dados_massa()
    product_b = factory.criar_ingrediente()
    product_b.dados_ingrediente()

    print("Massa: " + product_a.nome + " com " + product_b.nome)
    print("Valor: ")
    print(product_a.valor + product_b.valor)


if __name__ == "__main__":
    print("Criando Fusilli com molho branco")
    client_code(FusilliBranco())

    print("Criando Espaguete com milho")
    client_code(EspagueteMilho())