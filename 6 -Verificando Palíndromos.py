# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
