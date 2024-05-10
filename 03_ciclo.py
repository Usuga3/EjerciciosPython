#ciclo que pregunte 5 veces si los numeros son pares o impares

i=1
while i<=5:

    n1=int(input("digite un numero: "))
    if n1%2==0:
        print(n1,"es un numero par")
    else:
        print(n1,"es un numero impar")    
    i=i+1    