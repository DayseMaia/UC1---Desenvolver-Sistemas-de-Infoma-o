class Conta:
    def __init__(self, saldo, num_conta):
        self._saldo = saldo
        self._num_conta = num_conta

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("Saldo negativo!")
        else:
            self._saldo = novo_saldo
    
    def get_num_conta(self):
        return self._num_conta
    
    def set_num_conta(self, nova_conta):
        self._num_conta = nova_conta
        return nova_conta
    
conta1 = Conta(1000, "123456")

print(conta1.get_saldo())
print(conta1.get_num_conta())

conta1.set_saldo(-100)

print(conta1.get_saldo())
