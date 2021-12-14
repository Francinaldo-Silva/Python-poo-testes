"""visibilidades: __ private _ protected"""
class Veiculo():
    def __init__(self, cor, tp_combustivel, motor, qt_combustivel, is_ligado):
        self.__cor = cor
        self.__tp_combustivel = tp_combustivel
        self.__motor = motor
        self.__qt_combustivel = qt_combustivel
        self.__is_ligado =is_ligado

    def abastecer(self, qtcomb):
            self.__qt_combustivel += qtcomb

    def ligar(self):
            if self.__is_ligado:
                print("O veiculo está ligado")
            else:
                self.__is_ligado = True
                print("O veiculo está ligado")

    def desligar(self):
            if self.__is_ligado == False:
                print("O veiculo está desligado")
            else:
                self.__is_ligado = False