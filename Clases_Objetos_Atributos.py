'''La sintaxis de una clase comienza con la palabra class, seguida del nombre de la clase
y dos puntos. Dentro de la clase normalmente se encuentra el método __init__, 
que funciona como constructor. Este método se ejecuta automáticamente cada vez que se
crea un objeto.

Dentro del constructor aparece self, que representa al objeto actual. 
Gracias a self, cada objeto puede guardar sus propios datos. 
Cuando escribes algo como “self.nombre”, estás creando un atributo que pertenece
específicamente a ese objeto.'''

#Primera Clase
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

# Objetos de la primera clase
persona1 = Persona("Leo", 22, "Aguascalientes")
persona2 = Persona("Ana", 19, "Guadalajara")

#Segunda Clase
class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Objetos de la segunda clase
auto1 = Auto("Toyota", 2020, "Rojo")
auto2 = Auto("Honda", 2023, "Negro")

#Imprimiendo la primera clase
print(persona1.nombre, persona1.edad, persona1.ciudad)
print(persona2.nombre, persona2.edad, persona2.ciudad)

#Imprimiendo la segunda clase
print(auto1.marca, auto1.modelo, auto1.color)
print(auto2.marca, auto2.modelo, auto2.color)