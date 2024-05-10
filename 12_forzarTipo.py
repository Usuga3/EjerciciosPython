x=10 #cuando x vale 10 x es un int
#x=str(x) #aca cambia tipo de variable int a str
cadena= str(x) #cadena vale x, pero es srt
print ("x es un int, luego es un str y el valor no cambia:",cadena)
print("tipo de variable cadena: ",type(cadena))
print("tipo de variable x: ",type(x))




z="105"
#ejemplo de convertir un str a entero o decimal
x=int(z)
y=float(z)
b=bool(0) # convertir primero a int y luego a boolean


mensaje="str:{} ,int:{} , float:{} , boolean:{} ".format(z,x,y,b)
print("format print:",mensaje)


#sw=True
#if sw == True:
#   print("bombillo está {}",format(sw))