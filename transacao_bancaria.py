from conta import Conta
from datetime import datetime

class Transacao_Bancaria:
    def __init__(self,id_transacao: int, id_conta:int, data_hora: datetime,  tipo: str, valor: float) :
        self.id_transacao = id_transacao
        self.id_conta = id_conta
        self.data_hora= data_hora
        self.tipo = tipo
        self.valor = valor
        
    def id_transacaoGet(self):
        return self.id_transacao
    
    def id_transacaoSet(self, id_transacao):
        self.id_transacao = id_transacao
    
    def id_contaGet(self):
        return self.id_conta
    
    def id_contaSet(self, id_conta):
        self.id_conta = id_conta
        
    def data_horaGet(self):
        return self.data_hora
    
    def data_horaSet(self, data_hora):
        self.data_hora = data_hora
        
    def tipoGet(self):
        return self.tipo
    
    def tipoSet(self, tipo):
        self.tipo = tipo
    
    def valorGet(self):
        return self.valor
    
    def valorSet(self, valor):
        self.valor = valor
            