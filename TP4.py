"""1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
ingresado por parámetro."""

# def es_primo(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
# def primos(n):
#     prim=[]
#     for num in range(2,n+1):
#         if es_primo(num):
#             primos.append(num)
#     return prim
# numero=17
# primo=prim(numero)
# print("los numeros primos son",primo)

"""Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
programa de acuerdo a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución. """

# def sándwich():
#     condimentos=[]
#     while True:
#         condis=input("ingrese un condimento, si ya esta satisfecho ingrese salir:")
#         condimentos.append(condis)
#         print("ya se agrego al sándwich")
#         if condis=="salir":
#             condimentos.remove("salir")
#             break
#     print("los condimentos acutuales son",condimentos)        
# sándwich()     

"""Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).""" 

# def fibonacci(n):
#     serie=[0,1]
#     if n==0:
#         return n
#     elif n==1:
#         return n
#     else:
#         for i in range(2,n):
#             serie.append(serie[i-1]+serie[i-2])
#     return serie
# print(fibonacci(15))