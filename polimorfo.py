# Importar las clases de persona, hija_1 e hija_2 desde tarea2.py

from tarea2 import persona, hija_1, hija_2

# Crear una instancia de esas clases

persona1 = persona("Marcos","Perez",27,"M",180,"Estudiante")
print(persona1.get_name())
persona1.describir()

persona2 = hija_1("nickName","hobbie","motherName","firstName","lastName",30,"F",180,"ocupattion")
print(persona2.get_nickName())
persona2.describir()


persona3 = hija_2("nacionality","favoriteFood","favoriteColor","firstName","lastName",25,"M",180,"ocupattion")
print(persona3.get_nacionality())
persona3.describir()

#Esto sucede gracias a que las instancias o los objetos, son llamados por la clase correspondiente, es decir, la persona1 llama la clase persona, la persona2 llama a la clase hija_1 y finalmente la persona 3 llama a la clase hija_2. Cada una tiene su correspondiente método