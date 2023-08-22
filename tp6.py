""" Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo."""
# class Rectángulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura    
#     def calcular_area(self):
#         return self.base * self.altura
# base_rectangulo=float(input("base del rectángulo: "))
# altura_rectangulo = float(input("altura del rectángulo: "))
# mi_rectangulo = Rectángulo(base_rectangulo, altura_rectangulo)
# area = mi_rectangulo.calcular_area()
# print("El área del rectángulo es:", area)
"""Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.
"""
# class Mate:
#     def __init__(self, n):
#         self.n = n
#         self.cebadas_restantes = 0
#         self.lleno = False

#     def cebar(self):
#         if self.lleno:
#             raise Exception("¡Cuidado! ¡Te quemaste!")
        
#         if self.cebadas_restantes < self.n:
#             self.cebadas_restantes += 1
#             self.lleno = True
#             print("Mate cebado. Cebadas restantes:", self.cebadas_restantes)
#         else:
#             self.cebadas_restantes = 0
#             print("Advertencia: el mate está lavado.")

#     def beber(self):
#         if not self.lleno:
#             raise Exception("¡El mate está vacío!")

#         self.cebadas_restantes -= 1
#         if self.cebadas_restantes == 0:
#             self.lleno = False

#         if self.cebadas_restantes < 0:
#             print("Advertencia: el mate está lavado.")
#         else:
#             print("Bebiendo mate. Cebadas restantes:", self.cebadas_restantes)

# # Ejemplo de uso
# mate = Mate(3)

# for _ in range(5):
#     mate.cebar()
#     mate.beber()
"""Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho"""
# class Corcho:
#     def __init__(self, bodega):
#         self.bodega = bodega

# class Botella:
#     def __init__(self):
#         self.corcho = None

# class Sacacorchos:
#     def __init__(self):
#         self.corcho_sacado = None
    
#     def destapar(self, botella):
#         if self.corcho_sacado is not None:
#             raise Exception("El sacacorchos ya contiene un corcho.")
        
#         if botella.corcho is None:
#             raise Exception("La botella ya está destapada.")
        
#         self.corcho_sacado = botella.corcho
#         botella.corcho = None

#     def limpiar(self):
#         if self.corcho_sacado is None:
#             raise Exception("No hay un corcho en el sacacorchos para limpiar.")
        
#         corcho_limpio = self.corcho_sacado
#         self.corcho_sacado = None
#         return corcho_limpio

# corcho1 = Corcho("Bodega A")
# botella1 = Botella()
# botella1.corcho = corcho1

# corcho2 = Corcho("Bodega B")
# botella2 = Botella()
# botella2.corcho = corcho2

# sacacorchos = Sacacorchos()

# try:
#     sacacorchos.destapar(botella1)
#     print("Botella destapada. Corcho sacado de:", sacacorchos.corcho_sacado.bodega)
    
#     sacacorchos.destapar(botella2)
#     print("Botella destapada. Corcho sacado de:", sacacorchos.corcho_sacado.bodega)
# except Exception as e:
#     print("Error:", e)

# try:
#     corcho_limpio = sacacorchos.limpiar()
#     print("Corcho limpiado de:", corcho_limpio.bodega)
# except Exception as e:
#     print("Error:", e)
"""na heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. """
# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida
#     def describir_restaurante(self):
#         print("Restaurante:", self.restaurante_nombre)
#         print("Tipo de comida:", self.tipo_comida)
#     def abrir_restaurante(self):
#         print("¡El restaurante", self.restaurante_nombre, "está ahora abierto!")
# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores
#     def mostrar_sabores(self):
#         print("Sabores disponibles:")
#         for sabor in self.sabores:
#             print("-", sabor)
# sabores_heladeria = ["Vainilla", "Chocolate", "Fresa", "Mango", "Dulce de Leche"]
# heladeria_instancia = Heladeria("La Heladería Feliz", "Heladería", sabores_heladeria)
# heladeria_instancia.describir_restaurante()
# heladeria_instancia.mostrar_sabores()
# heladeria_instancia.abrir_restaurante()
"""Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada"""
# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad    
#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             raise Exception("El personaje ha sido derrotado.")  
#     def mover(self, direccion):
#         if direccion == "izquierda":
#             self.posicion -= self.velocidad
#         elif direccion == "derecha":
#             self.posicion += self.velocidad
# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque
#     def atacar(self, otro_personaje):
#         otro_personaje.recibir_ataque(self.ataque)
#         print("Soldado atacó con", self.ataque, "de daño.")
# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha     
#     def cosechar(self):
#         print("El campesino cosechó", self.cosecha, "unidades.")
#         return self.cosecha
# soldado = Soldado(100, 0, 10, 20)
# campesino = Campesino(50, 10, 5, 30)
# print("Posición inicial del campesino:", campesino.posicion)
# campesino.mover("derecha")
# print("Nueva posición del campesino:", campesino.posicion)
# soldado.atacar(campesino)
# print("Vida del campesino después del ataque:", campesino.vida)
# cosecha_obtenida = campesino.cosechar()
# print("Cantidad cosechada por el campesino:", cosecha_obtenida)
"""Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.
"""
# class Usuario:
#     def __init__(self, nombre, apellido, edad, correo):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.correo = correo
#     def describir_usuario(self):
#         print("Nombre:", self.nombre)
#         print("Apellido:", self.apellido)
#         print("Edad:", self.edad)
#         print("Correo:", self.correo)
#     def saludar_usuario(self):
#         print("¡Hola,", self.nombre, "!", "Bienvenido/a de nuevo.")
# usuario1 = Usuario("Juan", "Pérez", 30, "juan@example.com")
# usuario2 = Usuario("María", "González", 25, "maria@example.com")
# usuario3 = Usuario("Carlos", "López", 40, "carlos@example.com")
# print("Usuario 1:")
# usuario1.describir_usuario()
# usuario1.saludar_usuario()
# print()
# print("Usuario 2:")
# usuario2.describir_usuario()
# usuario2.saludar_usuario()
# print()
# print("Usuario 3:")
# usuario3.describir_usuario()
# usuario3.saludar_usuario()
"""Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""
# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, correo, privilegios):
#         super().__init__(nombre, apellido, edad, correo)
#         self.privilegios = privilegios
#     def mostrar_privilegios(self):
#         print("Privilegios del administrador:")
#         for privilegio in self.privilegios:
#             print("-", privilegio)

# privilegios_admin = ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
# admin = Admin("Admin", "Root", 0, "admin@example.com", privilegios_admin)

# admin.mostrar_privilegios()




