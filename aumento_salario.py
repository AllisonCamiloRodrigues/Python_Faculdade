salario = float(input("Digite seu salário:"))

percentual = float(input("Digite o percentual de aumento:"))

novo_salario = salario * (1 + percentual/100)

print(f"O meu salário é R${salario:.2f}, o percentual de aumento foi {percentual:.1f}% e o novo salario sera R${novo_salario:.2f}")