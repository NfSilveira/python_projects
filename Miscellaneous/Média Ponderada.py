peso1 = float(input("Digite o peso da primeira prova: "))
peso2 = float(input("Digite o peso da segunda prova: "))
nota1 = float(input("Digite sua nota na primeira prova: "))
nota2 = float(input("Digite sua nota na segunda prova: "))

mp = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)

print("A média ponderada é:", mp)

input("Aperte Enter para sair.")