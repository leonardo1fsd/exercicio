salario = float(input("Digite seu salário: R$ "))

def ajuste(salario):
    if salario >= 5000:
        realuste = salario * 10 / 100
        salario_realustado = salario + realuste
        return print(f"Seu salário sofre um realuste. Agora é: R$ {salario_realustado}")
    else:

        reajuste = salario * 15 / 100 
        salario_reajustado= salario + reajuste
        return print(f"Seu salário sofre um reajuste. Agora é: R$ {salario_reajustado}")
    

ajuste(salario)
