idade = int(input("Insira a sua idade: "))

if idade < 13:
    print("É uma criança")
elif idade >= 13 and idade <= 17:
    print("É um jovem")
elif idade >= 18 and idade <= 64:
    print("É um adulto")
else:
    print("É sénior")