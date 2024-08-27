#função com parametro e retorno (return)
def numero(num):
    if num % 2  ==0:
        return"par"
    else:
        return "impar"
resultado = numero(int (input("digite um numero: ")))
print(resultado)
