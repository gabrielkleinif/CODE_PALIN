print("Verificador de Palíndromo")

# solicita a palavra a ser verificada
palavra = input("Digite uma palavra: ")

# reverte a palavra
palavra_revertida = palavra[::-1]

# verifica se a palavra original e a palavra revertida são iguais
if palavra == palavra_revertida:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
