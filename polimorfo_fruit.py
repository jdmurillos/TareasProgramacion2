# Importar las clases de persona, hija_1 e hija_2 desde tarea2_fruit.py

from tarea2_fruit import Fruit, hija_1 , hija_2

fruta_1 = Fruit("orange","orange","circle","Sweet","warm","small")

fruta_2 = hija_2("orange","orange","circle","Sweet","warm","small","scientificName","producingCountry","originative")

fruta_3 = hija_2("orange", "orange", "circle", "sweet", "warm", "medium",30,10,1500)

print(fruta_1.get_color())
fruta_2.describir()

#Esto sucede gracias a que las instancias o los objetos, son llamados por la clase correspondiente, es decir, la persona1 llama la clase persona, la persona2 llama a la clase hija_1 y finalmente la persona 3 llama a la clase hija_2. Cada una tiene su correspondiente método

