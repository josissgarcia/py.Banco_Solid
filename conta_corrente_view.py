from conta_corrente import Conta_Corrente
class Conta_Corrente_View:
    
    def exibir_saldo_disponivel_para_saque(self, conta_corrente: Conta_Corrente):
            if conta_corrente.saldo_atual < 0:
                saldo_disponivel = conta_corrente.limite_cheque_especial - (conta_corrente.saldo_atual*-1)
                return (f'Saldo C/C: R$ {conta_corrente.saldo_atual: .2f}\nSaldo cheque especial: R$ {saldo_disponivel: .2f}\nSaldo total disponível: R$ {saldo_disponivel: .2f}')
            else :
                saldo_disponivel = conta_corrente.saldo_atual + conta_corrente.limite_cheque_especial
                return (f'Saldo C/C: R$ {conta_corrente.saldo_atual: .2f}\nSaldo cheque especial: R$ {conta_corrente.limite_cheque_especial: .2f}\nSaldo total disponível: R$ {saldo_disponivel: .2f}')
