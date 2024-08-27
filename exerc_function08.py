
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

def calculo(base, altura):
    area = (base * altura) / 2
    return area


resultado = calculo(base, altura)

#
print(f"A área do triângulo é: {resultado}")