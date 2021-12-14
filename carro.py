import transportes
class Carro(transportes.Veiculo):
    def __init__(self,cor, tp_combustivel, motor, qt_combustivel, is_ligado, qtp):
        super().__init__(cor, tp_combustivel,motor,qt_combustivel,is_ligado)
        self.qtp = qtp