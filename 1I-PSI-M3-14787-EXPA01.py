# #B1

# num = int(input("Digite um valor: "))

# if num >= 0:
#     print("O número é positivo")
# else:
#     print("O número é negativo")

# #B2

# idade = int(input("Indique a sua idade: "))

# if idade >= 18:
#     print("É maior de idade")
# else:
#     print("Não é maior de idade")

# #B3

# num2 = int(input("Digite um número:"))

# if num2 % 2 == 0:
#     print("O número é par")
# else:
#     print("O número é impar")

# #B4

# op1 = int(input("Indique o primeiro número: "))
# op2 = int(input("Indique o segundo número: "))

# if op1 > op2:
#     print(f"O maior número é o {op1}")
# elif op2 > op1:
#     print(f"O maior número é o {op2}")
# else:
#     print("Os números são iguais")

# #B5

# password = "python"

# pass_tentada = str(input("Digite a password: "))

# if pass_tentada == password:
#     print("Acesso permitido")
# else: 
#     print("Acesso negado")

# #I1

# nota = float(input("Digite a sua nota: "))

# if nota >= 18:
#     print("Excelente")
# elif nota >= 14:
#     print("Bom")
# elif nota >= 10:
#     print("Suficiente")
# else:
#     print("Reprovado")

# #I2

# idade2 = int(input("Digite a sua idade: "))

# if idade2 < 13:
#     print("Criança")
# elif idade2 >= 13 and idade2 < 18:
#     print("Jovem")
# elif idade2 >= 18 and idade2 < 65:
#     print("Adulto")
# else:
#     print("Sénior")

# #I3

# x = int(input("Indique um número: "))

# if x % 3 == 0 and x % 5 == 0:
#     print("O número é múltiplo de ambos 3 e 5")
# elif x % 3 == 0:
#     print("O número é multiplo de 3")
# elif x % 5 == 0:
#     print("O número é multiplio de 5")
# else:
#     print("O número não é multiplo de nem 3 nem 5")

# #I4

# user_certo = ("admin")
# password_correta = 1234

# user = str(input("Digite o utilizador: "))
# password = int(input("Digite a password: "))

# if user != user_certo:
#     print("Utilizador errado")
# elif password != password_correta:
#     print("Passoword errada")
# elif user == user_certo and password == password_correta:
#     print("Utilizador e password corretos")

# #I5

# num_intervalo = float(input("Digite um número: "))

# if num_intervalo >= 10 and num_intervalo <= 20:
#     print("O número está dentro do intervalo")
# else:
#     print("O número não está dentro do intervalo")

# #A1

# saldo_inicial = 1000
# valor_a_levantar = float(input("Digite o valor a levantar: "))

# if valor_a_levantar <= saldo_inicial:
#     print("Levantamento autorizado")
# else:
#     print("Saldo insufuciente")

# #A2

# x1 = int(input("Indique o primeiro valor: "))
# x2 = int(input("Indique o segundo valor: "))
# x3 = int(input("Indique o terceiro valor: "))
# x4 = int(input("Indique o quarto valor: "))

# if x1 > x2 and x1 > x3 and x1 > x4:
#     print(f"O maior número é o {x1}")
# elif x2 > x1 and x2 > x3 and x2 > x4:
#     print(f"O maior número é o {x2}")
# elif x3 > x1 and x3 > x2 and x3 > x4:
#     print(f"O maior número é o {x3}")
# elif x4 > x1 and x4 > x2 and x4 > x3:
#     print(f"O maior número é o {x4}")

# #A3

# peso = float(input("Digite o seu peso: "))
# altura = float(input("Digite a sua altura: "))
# IMC = peso / (altura * altura)

# if IMC < 18.5:
#     print("Baixo peso")
# elif IMC >= 18.5 and IMC <= 24.9:
#     print("Peso normal")
# elif IMC >= 25 and IMC <= 29.9:
#     print("Exceso de peso")
# else:
#     print("Obesidade")

# #A4

# valor_compra = int(input("Qual é o valor da compra: "))
# desconto = 0
# if valor_compra >= 100:
#     desconto = 100 * 0.1
#     valor_final = valor_compra - desconto
#     print(f"O seu desconto é {desconto} e vai pagar {valor_final}")
# elif valor_compra >= 50:
#     desconto = 50 * 0.05
#     valor_final = valor_compra - desconto
#     print(f"O seu desconto é de {desconto} e vai pagar {valor_final}")
# else: print(f"Não tem nenhum desconto e vai pagar {valor_compra}")

# #A5

# ano = int(input("Indique um ano: "))

# if ano % 4 == 0:
#     print(f"O ano {ano} é bissexto")
# else:
#     print(f"O ano {ano} é um ano normal")