def contador (inicio,fim,passo):
    if passo ==0:
        print("o passo nao pode ser zero")
        return
    if passo>0:
        if inicio> fim:
            print("o inicio deve ser menor ou igual ao fim para passos positivos")
            return
        for i in range (inicio,fim + 1, passo):
            print (i, d='')
        print()

    elif passo<0:
        if inicio< fim:
            print("o inicio deve ser maior ou igual ao fim para passos negativos")
            return
        for i in range (inicio,fim -1, passo):
            print (i,end='')
        print()
try:
    inicio= int (input("digite o vlaor de inicio:"))
    fim = int ( input("digite o valor de fim: "))
    passo = int( input( "digite o valor do passo:"))
    
    contador(inicio,fim, passo)
except ValueError:
    print(" por favor, digite apenas numeros inteiros")