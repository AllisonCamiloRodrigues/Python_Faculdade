caixa = {"Alface": 5.00,
    "Tomate": 8.30,
    "Limão": 4.45,
    "Banana": 5.67 
}
total = 0

while True:

    item = input("digite qual item vocè quer adicionar:")

    quantidade = int(input(f"Digite a quantidade de {item}"))

    SubTotal = caixa.get(item) * quantidade #Consulta o que está na tabela e multiplica pela quantidade

    total += SubTotal

    sair = input("Gostaria de Finalizar")
    if sair == "sim":
        print(f"O valor total é R$ {total:.2f}")
        break
    elif sair == "não":
        continue
    



