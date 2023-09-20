student_name = input("Digite o nome do aluno: ")

score_validation = False
absence_validation = False

while score_validation == False:
    first_test_score = input("Digite a nota do aluno na primeira prova: ")
    try:
        first_test_score = float(first_test_score)
        if first_test_score < 0 or first_test_score > 10:
            print("Nota inválida. O valor deve ser entre 0 e 10.")
        else:
            score_validation = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com '.'. (Ex.: 9.5)")

score_validation = False

while score_validation == False:
    second_test_score = input("Digite a nota do aluno na segunda prova: ")
    try:
        second_test_score = float(second_test_score)
        if second_test_score < 0 or second_test_score > 10:
            print("Nota inválida. O valor deve ser entre 0 e 10.")
        else:
            score_validation = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com '.'. (Ex.: 9.5)")


while absence_validation == False:
    absence_amount = input("Digite o número de faltas do aluno: ")
    try:
        absence_amount = float(absence_amount)
        if absence_amount < 0 or absence_amount > 20:
            print("Número de faltas inválido. O valor deve ser entre 0 e 20.")
        else:
            absence_validation = True
    except:
        print("Número de faltas inválido. Use apenas números e separe os decimais com '.'. (Ex.: 15.5)")


test_average = (first_test_score + second_test_score) / 2
attendance = (20 - absence_amount) / 20

if test_average >= 6 and attendance >= 0.7:
    result = "O aluno foi aprovado."

elif test_average < 6 and attendance < 0.7:
    result = "O aluno foi reprovado por média e por faltas."

elif test_average < 6:
    result = "O aluno foi reprovado por média."

elif attendance < 0.7:
    result = "O aluno foi reprovado por faltas."

print('Nome:', student_name)
print('Média:', test_average)
print('Assiduidade:', str(attendance * 100) + '%')
print('Resultado:', result)