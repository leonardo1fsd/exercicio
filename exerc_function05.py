num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))
num3 = int(input("digite o terceiro valor: "))

maior = num1
if(num2> maior):
    maior = num2
if (num3> maior):
    maior = num3

    print('maior:', maior)

    menor = num1
    
if(num2> menor):
    menor = num2
if (num3> menor):
    menor = num3
    print('menor: ',menor)