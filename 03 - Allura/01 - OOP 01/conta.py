class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}.')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f'R$ {valor} reais sacado com sucesso.')
        else:
            print(f'O valor {valor} passou do limite.')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print(f'Foi transferido R$ {valor} da conta {self._Conta__titular} para conta {destino._Conta__titular}.')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print(f'Seu novo limite é {limite}')

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104','Bradesco': '237'}



conta_01 = Conta(1, 'João', 500.00, 5.000)
conta_02 = Conta(2, 'Marcos', 300.00, 2.000)


conta_02.extrato()
conta_01.extrato()
conta_01.transfere(200, conta_02)
conta_02.extrato()
conta_01.extrato()