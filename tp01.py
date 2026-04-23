saldo = 100
valor_levantar = float(input("Qual é o valor que quer levantar? "))
restante = saldo - valor_levantar

if valor_levantar <= saldo:
    print("Levantamento autorizado")
    print(f"Levantaste {valor_levantar} e o saldo restante é {restante}")
else:
    print(f"Saldo insuficiente, ficas com um saldo negativo de {restante}")