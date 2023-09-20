months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
birthdate = input("Digite a sua data de nascimento no formato DD-MM-AAAA: ")

index = int(birthdate[3:5])
month = months[index - 1]

print(f"Você nasceu no Mês de {month}.")