def aumento_salarial(salario, cargo):
    if cargo == "junior":
        return salario * 1.1
    elif cargo == "Pleno":
        return salario * 1.2
    elif cargo == "senior":
        return salario * 1.3
    
a = aumento_salarial(1000, "senior")
print(a)