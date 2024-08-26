def calculadora(num1, num2, op):
    print('Bienvenido a la calculadora de python'.center(50, '_'))
    if op == 1:
        print(num1 + num2)
    elif op == 2:
        print(num1 - num2)
    elif op == 3:
        print(num1 * num2)
    elif op == 4:
        print(num1 / num2)
    else:
        print("Te equivocaste de opción")

var1 = float(input('Introduzca el primer valor: '))
var2 = float(input('Introduzca el segundo valor: '))
opcion1 = int(input('Introduzca la opción (1: suma, 2: resta, 3: multiplicación, 4: división): '))
calculadora(var1, var2, opcion1)







