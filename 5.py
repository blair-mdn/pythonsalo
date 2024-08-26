#calcular el producto de todos los n numeros ingresados,
#el producto de los pares y el producto de los impares

n=int(input("ingrese la cantidad: "))
i=1
producto=1
impar=1
par=1
for i in range(n):
    num=int(input("ingrese el numero : "))
    producto=producto*num
    if num%2 !=0:
        impar=impar*num
    else:
        par=par*num
print("el producto de todos los numeros es: ", producto)
print("el producto de todos los numeros pares es: ", par)  
print("el producto de todos los numeros impares es: ", impar)              