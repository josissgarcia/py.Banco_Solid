from abc import abstractmethod

class Conta:
    def __init__(self, id_conta:int, saldo_atual:float) :
        self.id_conta: int = id_conta
        self.saldo_atual: float = saldo_atual
        
    def id_contaGet(self):
        return self.id_conta
    
    def id_contaSet(self, id_conta):
        self.id_conta = id_conta 
        
    def saldo_atualGet(self):
        return self.saldo_atual
    
    def saldo_atualSet(self, saldo_atual):
        self.saldo_atual = saldo_atual      
    
    @abstractmethod    
    def depositar(self, valor_a_ser_depositado:float):
        pass
    
    @abstractmethod  
    def sacar(self, valor_a_ser_sacado:float):
        pass
    
    @abstractmethod  
    def consultar_saldo_atual(self):
        pass