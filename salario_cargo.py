salario = float(input("Digite seu salário:"))

cargo = str("Digite seu cargo(junior, pleno ou senior)")

if cargo == "junior":
    novo_salario = salario * 1.1
elif cargo == "pleno":
    novo_salario = salario * 1.2
elif cargo == "senior":
    novo_salario = salario * 1.3
else:
    print("Cargo não identificado")

print(f"Seu cargo é: {cargo} e seu salario é {novo_salario}")