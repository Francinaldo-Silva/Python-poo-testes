class Carro():
    def __init__(self, cor, qtp, tp_combustivel, motor, qt_combustivel, is_ligado):
        self.cor = cor
        self.qtp = qtp
        self.tp_combustivel = tp_combustivel
        self.motor = motor
        self.qt_combustivel = qt_combustivel
        self.is_ligado =is_ligado
    def abastecer(self, qtcomb):
        self.qt_combustivel += qtcomb
    def ligar(self):
        if self.is_ligado :
            print("O carro está ligado")
        else:
            self.is_ligado = True
            print("O carro está ligado")
    def desligar(self):
        if self.is_ligado == False:
            print("O carro está desligado")
        else:
            self.is_ligado = False
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = None
        self.idade = None
        if __name__ == "__main__":
            p = Pessoa()
            p.nome = input()
            p.idade = input()
            print(f"Nome: {p.nome} - Idade: {p.idade}")
