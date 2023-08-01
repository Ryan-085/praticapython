# Solicita o valor da conta
valor_conta = float(input("Digite o valor da conta: "))

# Realiza o cálculo do acréscimo de 10%
acrescimo = valor_conta * 0.1

# Calcula o valor total da conta com o acréscimo

valor_total = valor_conta + acrescimo

# Exibe o valor total da conta
print(f"O valor total da conta, com o acréscimo de 10%, é: R${valor_total:.2f}")