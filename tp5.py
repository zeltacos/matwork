"""1) Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3). """
# def redondear(numero):
#     redond=round(numero)
#     return (redond)
# # numero = 4.51
# # resultado=redondear(numero)
# # print(f"El número {numero} redondeado es: {resultado}")

"""3) Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema"""
# import datetime
# fecha_hora_actual = datetime.datetime.now()
# formato = "%Y-%m-%d %H:%M:%S"  
# fecha_hora_formateada = fecha_hora_actual.strftime(formato)
# print("La fecha y hora actuales son:", fecha_hora_formateada)
"""4)Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)."""
# import random

# while True:
#     numero_par = random.randint(2, 10)  # Genera un número al azar entre 2 y 10
#     if numero_par % 2 == 0:
#         print("Número par generado:", numero_par)
#         break 
"""5)Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica."""
# import random

# def magic_8_ball():
#     responses = [
#         "Es seguro que sí",
#         "Las chances son buenas",
#         "Puedes contar con ello",
#         "Pregúntame de nuevo más tarde",
#         "Concéntrate y pregunta de nuevo",
#         "No veo con claridad, intenta de nuevo",
#         "Mi respuesta es no",
#         "Mis fuentes me dicen que no"
#     ]
#     return random.choice(responses)
# pregunta = input("Hazme una pregunta: ")
# respuesta = magic_8_ball()
# print("La bola mágica dice:", respuesta)

