#calcular la suma de los cuadrados de los n primeros numeros naturales,
#teniendo en cuenta que los n numeros deben ser positivos

n=int(input("ingrese la cantidad de numneros naturales :"))
while n<=0:
    print("el numero debe ser postivo")
    n=int(input("ingrese la cantidad de numneros naturales :"))
suma=0
for i in range(1,n+1):
    elevar_cuadrado=i*i
    suma= suma+ elevar_cuadrado
print("la suma de los n numeros naturales es: ", suma)