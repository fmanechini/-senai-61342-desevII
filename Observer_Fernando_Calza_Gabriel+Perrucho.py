from abc import ABC, abstractmethod

class Subject(ABC):
 
    @abstractmethod
    def addObserver(self, observer):
        pass
    
    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade, pressao):
        pass

class EstacaoMeteorologica(Subject):

    def __init__(self):
        self.observers = []
    
    def setMedicoes(self, temperatura, umidade, pressao):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.notifyObserver()
    
    def addObserver(self, observer):
        self.observers.append(observer)
    
    def removeObserver(self, observer):
        self.observers.remove(observer)
    
    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.temperatura, self.umidade, self.pressao)
    
class Estatisticas(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.addObserver(self)

    def mostrar(self):
        print("Temperatura: " + str(self.temperatura))
        print("Umidade: " + str(self.umidade))
        print("Pressao: " + str(self.pressao))
    
    def update(self, temperatura, umidade, pressao):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.mostrar()

if __name__ == "__main__":
    estacao = EstacaoMeteorologica()
    estatisticas = Estatisticas(estacao)

    estacao.setMedicoes(30, 45, 15)
    estacao.setMedicoes(35, 60, 22)
    estacao.setMedicoes(32, 70, 27)

