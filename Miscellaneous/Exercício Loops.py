repeat = "s"
invoice = []
total = 0
price_validation = False

while repeat == "s":
    product_name = input("Digite o nome do produto: ")

    while price_validation == False:
        product_price = input("Digite o preço do produto: ")
        try:
            product_price = float(product_price)
            if product_price <= 0:
                print("O preço precisa ser maior do que 0.")
            else:    
                price_validation = True
        except:
            print("Formato de preço inválido. Use apenas números e separe os centavos com '.'.")


    invoice.append([product_name, product_price])
    total += product_price
    price_validation = False

    repeat = input("Você deseja comprar mais algum produto?(S/N): ").lower()

for products in invoice:
    print(products[0], "-", products[1])


print("O total da fatura é:", total)