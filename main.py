import os
from conta_poupanca import Conta_Poupanca
from conta_corrente import Conta_Corrente
from conta_poupanca_view import Conta_Poupanca_View
from conta_corrente_view import Conta_Corrente_View
from conta import Conta

def main():
    
    conta_corrente = Conta_Corrente (id_conta=2, saldo_atual=500.00, limite_cheque_especial=1000.00)
    consultar_saldo_corrente = Conta_Corrente_View()
   
    poupanca = Conta_Poupanca(id_conta=1, saldo_atual=2500.00, taxa_de_rendimento_ao_ano= 15.00)
    consultar_saldo_poupanca = Conta_Poupanca_View()

    opcao = ""
    while opcao != "Sair":
        opcao = input ("""
        [ 1 ] Depósito em conta corrente
        [ 2 ] Saque em conta corrente
        [ 3 ] Consulta saldo disponivel em conta corrente
        [ 4 ] Depósito em conta poupança
        [ 5 ] Saque em conta poupança
        [ 6 ] Consulta saldo em conta poupança
        [ 7 ] Visualiza rendimentos
        [ 8 ] Sair
        Digite a opção desejada:   """)
        
        match opcao:
            case '1': 
                valor_do_deposito = input("\nValor a ser depositado na conta corrente: ")
                print(f'{conta_corrente.depositar(valor_do_deposito)}\n{consultar_saldo_corrente.exibir_saldo_disponivel_para_saque(conta_corrente)}')
            case '2':
                valor_do_saque = input('\nValor a ser sacado da conta corrente: ')
                print(f'{conta_corrente.sacar(valor_do_saque)}\n{consultar_saldo_corrente.exibir_saldo_disponivel_para_saque(conta_corrente)}')
            case '3':
                print(consultar_saldo_corrente.exibir_saldo_disponivel_para_saque(conta_corrente))
            case '4':
                valor_do_deposito = input("\nValor a ser depositado na poupança: ")
                print(f'{poupanca.depositar(valor_do_deposito)}\n{consultar_saldo_poupanca.exibir_saldo_atual(poupanca)}')
            case '5':
                valor_do_saque = input('\nValor a ser sacado na poupança: ')
                print(f'{poupanca.sacar(valor_do_saque)}\n{consultar_saldo_poupanca.exibir_saldo_atual(poupanca)}')
            case '6':
                print(consultar_saldo_poupanca.exibir_saldo_atual(poupanca))
            case '7':
                periodo = input("""
        PERIODO PARA CALCULO DE RENDIMENTOS:
        [1] - Ano 
        [2] - Mês
        [3] - Semana
        [4] - Dia
        [5] - Horas
        [6] - Minutos 
        [7] - Segundos
        Digite o periodo desejado:  """)
                print(poupanca.calcular_rendimento(periodo))
            case '8':
                opcao = 'Sair'
            case _:
                print("[ ERRO: Opção inválida ]")  

if __name__=='__main__':
    os.system("cls")
    main()