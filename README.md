### 📗 Módulo 3 – Exercícios em Python
Este repositório reúne um conjunto de exercícios desenvolvidos em Python, realizados no contexto do Módulo 3 (Programação).
Ao longo das fichas são trabalhados vários conceitos essenciais, como lógica de programação, condições, ciclos e tratamento de dados de entrada.

### 🗂️ Organização do Repositório
Os exercícios encontram-se distribuídos por diferentes ficheiros, cada um dedicado a uma tarefa específica:
🔹 Fichas Iniciais (Básicas)

## FIcha 1
ex01-Ficha1.py → Apresentação de mensagens/dados no ecrã

ex02-Ficha1.py → Introdução de informação (nome e idade)

exp03-Ficha1.py → Estimativa de idade aproximada a partir de dados

## Ficha 2
ex01-Ficha2.py → Cálculo da soma de números inseridos pelo utilizador

ex02-Ficha2.py → Conversão de temperatura (°C para °F)

ex03-Ficha2.py → Operações matemáticas básicas (soma, subtração, etc.)

## Ficha 3
ex01-Ficha3.py → Verificação de aprovação (nota igual ou superior a 10)

ex02-Ficha3.py → Identificação de número par ou ímpar

ex03-Ficha3.py → Sistema de login com validação simples

## Ficha 4
ex01-Ficha4.py → Simulação simples de um levantamento bancário

ex02-Ficha4.py → Classificação por escalões de idade

ex03-Ficha4.py → Determinação do maior valor entre três números

ex04-Ficha4.py → Aplicação de descontos com base em condições

## A01

# B – Condições Simples
B1 — Pede um número e indica se é positivo ou negativo.
B2 — Pede a idade e diz se a pessoa é maior de idade (≥18) ou não.
B3 — Pede um número e verifica se é par ou ímpar.
B4 — Pede dois números e mostra qual é o maior (ou se são iguais).
B5 — Pede uma password e valida se está correta (acesso permitido/negado).

# I – Condições Encadeadas e Validações Mais Completas
I1 — Pede uma nota e classifica (Excelente / Bom / Suficiente / Reprovado).
I2 — Pede a idade e classifica por faixa etária (Criança / Jovem / Adulto / Sénior).
I3 — Pede um número e verifica se é múltiplo de 3, de 5 ou de ambos.
I4 — Pede utilizador e password e valida o login (deteta qual está errado).
I5 — Pede um número e verifica se está entre 10 e 20 (inclusive).

# A  – problemas um Pouco Mais Longos e Com Cais Regras
A1 — Simula um levantamento: compara o valor pedido com um saldo inicial e autoriza ou recusa.
A2 — Pede 4 números e indica qual é o maior.
A3 — Calcula o IMC a partir do peso e altura e dá a categoria correspondente.
A4 — Pede o valor da compra e aplica desconto consoante o total (ou nenhum desconto).
A5 — Pede um ano e diz se é bissexto ou normal (regra usada: divisível por 4).

## A02

# B – Condições Simples
B1 — Mostra os números de 1 a 10 usando um ciclo while.
B2 — Mostra os números de 10 até 1 (contagem decrescente) com while.
B3 — Imprime os números de 0 a 20 usando um ciclo for.
B4 — Imprime apenas os números pares de 0 a 20 usando for com salto de 2.

# I – Condições Encadeadas e Validações Mais Completas
I1 — Calcula a soma acumulada de 1 até 100 e vai mostrando o valor da soma ao longo do processo.
I2 — Pede números ao utilizador até ser introduzido um número negativo; quando isso acontece, termina o programa.
I3 — Mostra os números pares de 0 a 50 e pretende contar quantos pares existem (no final imprime o total).

# A  – problemas um Pouco Mais Longos e Com Cais Regras
A1 — Pergunta quantos números o utilizador quer inserir e depois calcula a soma total desses números.
A2 — Faz um menu repetitivo: permite escolher entre mostrar 1 a 10, mostrar pares até 20, ou sair.
A3 — Pede um número e calcula o seu fatorial (multiplicação de 1 até ao número).

## A03

Este programa é um pequeno sistema de gestão de notas com um menu. Ele permite:

Adicionar notas (com validação entre 0 e 20)
Listar todas as notas guardadas
Calcular a média das notas
Mostrar apenas notas positivas (≥ 10)
Sair do programa

Ele fica a correr em ciclo até o utilizador escolher 0.

## A04

Este programa permite:

Adicionar materiais novos ao stock com uma quantidade inicial
Consultar a quantidade de um material específico
Atualizar o stock de um material existente (adicionar ou remover unidades)
Ver o stock completo (lista de todos os materiais e quantidades)
Sair do sistema quando o utilizador quiser

Tudo isto acontece num ciclo: o menu aparece várias vezes e o programa só termina quando escolheres a opção de sair.
