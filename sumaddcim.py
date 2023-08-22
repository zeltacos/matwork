"""2) Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado."""
from tp5 import redondear
def suma(a,b):
    numero=a+b
    return (numero)
numero1=5.16
numero2=2.41
resultado=suma(numero1,numero2)
redondeo=redondear(resultado)
print(f"el resultado de la suma de {numero1,numero2} es {resultado} y redondeado es {redondeo}")


