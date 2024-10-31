#Estrutura Condicional Simples

numero1 = 2
numero2 = 2

if numero1 > numero2:
    print("O número 1 é maior que o número 2") 
else:
    print("O número 2 é maior que o número 1")

# Estrutura Condicional Aninhada
soma = 1 

if soma > 0:
    print("A soma é maior que zero")
elif soma == 0:
    print("A soma é igual a zero")
else:
    print("A soma é menor que zero")

# Estrutura de Repetição For
for i in range(10):
    print(i)

lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

# Estrutura de Repetição com Condição
for i in range(10):
    if i == 5:
        print("O valor de i é 5")
    else:
        print(i)

# Estrutura de Repetição com Condição e Break
for i in range(10):
    if i == 5:
        break
    print(i)

# Estrutura de Repetição com Condição e Continue
for i in range(10):
    if i == 5:
        continue
    print(i)

# Estrutura de Repetição com Condição e Else
for i in range(10):
    if i == 5:
        break
    print(i)
else:   
    print("Fim do loop")

# Estrutura de Repetição com While
contador = 0
while contador < 10:
    print(f'valor do contador é {contador}')
    contador += 1

# Estrutura de Repetição com While e Break
contador = 0
while contador < 10:
    print(f'valor do contador é {contador}')
    contador += 1
    if contador == 5:
        break

# Estrutura de Repetição com While e Continue
contador = 0
while contador < 10:
    print(f'valor do contador é {contador}')
    contador += 1
    if contador == 5:
        continue
# Estrutura de Repetição com While e Else
contador = 0
while contador < 10:
    print(f'valor do contador é {contador}')
    contador += 1
else:
    print("Fim do loop")

