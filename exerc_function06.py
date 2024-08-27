


nome = str(input(f"digite seu nome: "))
idade = int(input(f"digite sua idade: "))

def confir(idade):
    if idade>=18:
        print("você é maior de idade")
    else:
        print("você é menor de idade")


print (confir(idade))