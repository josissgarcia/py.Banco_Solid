from conta import Conta
from validacao_valor import Validacao_Valor

class Conta_Corrente(Conta):
    def __init__(self, id_conta: int, saldo_atual: float, limite_cheque_especial: float):
        super().__init__(id_conta, saldo_atual)
        self.limite_cheque_especial = limite_cheque_especial
        
    def limite_cheque_especialGet(self):
        return self.limite_cheque_especial 
    
    def limite_cheque_especialSet(self, limite_cheque_especial):
        self.limite_cheque_especial = limite_cheque_especial  

    
    def depositar(self, valor: str):
        validacao = Validacao_Valor()
            
        if validacao.valida_valor(valor) == True:
            valor_a_ser_depositado = float(valor)
            self.saldo_atual += valor_a_ser_depositado
            return "[ Deposito realizado com sucesso! ]"
        else:
            return "[ ERRO: Valor inválido ]"
    
    def sacar(self, valor: str):
        validacao = Validacao_Valor()
        
        if validacao.valida_valor(valor) == True:
            valor_a_ser_sacado = float(valor)
            saldo_total_disponivel = self.limite_cheque_especial + self.saldo_atual
            
            if valor_a_ser_sacado <= saldo_total_disponivel:
                self.saldo_atual -= valor_a_ser_sacado
                return "[ Saque realizado com sucesso! ]"
            
            else:
                return "[ Saldo insuficiente para saque ]"
            
        else:
            return "[ ERRO: Valor inválido ]"        