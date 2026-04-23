valor_compra = int(input("Qual é o valor da compra: "))
desconto = 0
if valor_compra >= 100:
    desconto = 100 * 0.1
    valor_final = valor_compra - desconto
    print(f"O seu desconto é {desconto} e vai pagar {valor_final}")
elif valor_compra >= 50:
    desconto = 50 * 0.05
    valor_final = valor_compra - desconto
    print(f"O seu desconto é de {desconto} e vai pagar {valor_final}")
else: print(f"Não tem nenhum desconto e vai pagar {valor_compra}")