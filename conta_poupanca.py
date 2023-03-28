from conta import Conta
from validacao_valor import Validacao_Valor

class Conta_Poupanca(Conta):
    def __init__(self, id_conta: int, saldo_atual: float, taxa_de_rendimento_ao_ano: float):
        super().__init__(id_conta, saldo_atual)
        self.taxa_de_rendimento_ao_ano = taxa_de_rendimento_ao_ano
    
    def taxa_de_rendimento_ao_anoGet(self):
        return self.taxa_de_rendimento_ao_ano
    
    def taxa_de_rendimento_ao_anoSet(self, taxa_de_rendimento_ao_ano):
        self.taxa_de_rendimento_ao_ano = taxa_de_rendimento_ao_ano

    
    def depositar(self, valor: str):
        validacao = Validacao_Valor()

        if validacao.valida_valor(valor)== True:            
            valor_a_ser_depositado = float(valor)
            self.saldo_atual += valor_a_ser_depositado
            return "[ Deposito realizado com sucesso! ]"
        else:
            return "[ ERRO: Valor inválido ]"
    
    def sacar(self, valor: str):
        validacao = Validacao_Valor()
        
        if validacao.valida_valor(valor) == True: 
            valor_a_ser_sacado = float(valor)
            
            if self.saldo_atual >= valor_a_ser_sacado:
                self.saldo_atual -= valor_a_ser_sacado
                return "[ Saque realizado com sucesso! ]"
            else:
                return "[ Saldo insuficiente ]"
        else:
            return "[ ERRO: Valor inválido ]"
        
    def calcular_rendimento(self, periodo):
        rendimento = self.saldo_atual * (self.taxa_de_rendimento_ao_ano / 100)
        match periodo:
            case "1": # Ano
                return (f'Valor do rendimento ao ano: R$ {rendimento:.2f}')
            case "2": # Mes
                return (f'Valor do rendimento ao mês: R$ {(rendimento / 12):.2f}')
            case "3": # Semana
                return (f'Valor do rendimento por semana: R$ {rendimento / 52:.2f}')
            case "4": # Dia
                return (f'Valor do rendimento ao dia: R$ {rendimento / 365:.2f}')
            case "5": # Horas
                return (f'Valor do rendimento por hora: R$ {rendimento / (365 * 24):.4f}')
            case "6": # Minutos
                return (f'Valor do rendimento por minuto: R$ {rendimento / (364 * 24 * 60):.4f}')
            case "7": # Segundos
                return (f'Valor do rendimento por segundo: R$ {rendimento / (364 * 24 * 60 * 60):.6f}')
            case _:
                return "[ ERRO: Opção inválida ]"   

