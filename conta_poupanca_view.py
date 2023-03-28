from conta_poupanca import Conta_Poupanca

class Conta_Poupanca_View: 
    
    def exibir_saldo_atual(self, poupanca:Conta_Poupanca):
        return (f'Saldo Poupança: R$ {poupanca.saldo_atual: .2f}')