def bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def bmi_class(gender, weight, height):
    bmi_value = bmi(weight, height)

    if gender == "m":
        if bmi_value < 20.7:
            return "Abaixo do Peso.\n"
        elif bmi_value >= 20.7 and bmi_value < 26.4:
            return "Peso Normal.\n"
        elif bmi_value >= 26.4 and bmi_value < 27.8:
            return "Marginalmente Acima do Peso.\n"
        elif bmi_value >= 27.8 and bmi_value < 31.1:
            return "Acima do Peso Ideal.\n"
        elif bmi_value >= 31.1:
            return "Obesidade.\n"
        else:
            return "Erro de cálculo. Entre em contato com o administrador.\n"
    
    if gender == "f":
        if bmi_value < 19.1:
            return "Abaixo do Peso.\n"
        elif bmi_value >= 19.1 and bmi_value < 25.8:
            return "Peso Normal.\n"
        elif bmi_value >= 25.8 and bmi_value < 27.3:
            return "Marginalmente Acima do Peso.\n"
        elif bmi_value >= 27.3 and bmi_value < 32.3:
            return "Acima do Peso Ideal.\n"
        elif bmi_value >= 31.3:
            return "Obesidade.\n"
        else:
            return "Erro de cálculo. Entre em contato com o administrador.\n"

print("Vamos calcular seu IMC?")

gender_validation = False

while gender_validation == False:
    gender = input("Digite o seu sexo(M ou F): ").lower()
    if gender != "m" and gender != "f":
        print("Sexo inválido. Digite M ou F.")
    else:
        gender_validation = True
        print("\n")


weight_validation = False

while weight_validation == False:
    weight = input("Digite o peso (Ex.: 68.5): ")
    try:
        weight = float(weight)
        if weight <= 0:
            print("Peso inválido. O número não pode ser 0 ou negativo.")
        else:
            weight_validation = True
            print("\n")
    except:
        print("Peso inválido. Use apenas números e separe os decimais com '.'. (Ex.: 68.5)")

height_validation = False

while height_validation == False:
    height = input("Digite a altura em metros (Ex.: 1.70): ")
    try:
        height = float(height)
        if height <= 0 or height > 3:
            print("Altura inválida. O número não pode ser 0 ou negativo e deve ser inferior a 3 metros.")
        else:
            height_validation = True
            print("\n")
    except:
        print("Altura inválida. Use apenas números e separe os decimais com '.'. (Ex.: 1.70)")

v_bmi = str(bmi(weight, height))
c_bmi = bmi_class(gender, weight, height)

print("O seu IMC é:", v_bmi[0:5])
print("A sua classificação é:", c_bmi)