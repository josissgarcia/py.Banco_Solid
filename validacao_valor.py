class Validacao_Valor: 
    
    def valida_valor(self, valor_str):
        try:
            valor = float(valor_str)
            if valor >= 0:
                return True
            else:
                return "[ ERRO: Valor negativo ]"
            
        except ValueError as ve:
            return "[ ERRO: Valor não é numérico]"
        
    