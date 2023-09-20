student_name = input("Digite o nome do aluno: ")

first_test_score = float(input("Digite a nota do aluno na primeira prova: "))
second_test_score = float(input("Digite a nota do aluno na segunda prova: "))
absence_amount = int(input("Digite o número de faltas do aluno: "))

test_average_score = (first_test_score + second_test_score) / 2
attendance = (20 - absence_amount) / 20

if test_average_score >= 6 and attendance >= 0.7:
    result = "O aluno foi aprovado."

elif test_average_score < 6 and attendance < 0.7:
    result = "O aluno foi reprovado por média e por faltas."

elif test_average_score < 6:
    result = "O aluno foi reprovado por média."

elif attendance < 0.7:
    result = "O aluno foi reprovado por faltas."

else:
    print("Ocorreu um erro.")

print('Nome:', student_name)
print('Média:', test_average_score)
print('Assiduidade:', str(attendance * 100) + '%')
print('Resultado:', result)