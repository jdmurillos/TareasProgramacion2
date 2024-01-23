#Class Fruit

class Fruit:
    def __init__(self,name,color,shape,taste,weather,size):
        self.__name= name
        self.__color= color
        self.__shape= shape
        self.__taste= taste
        self.__weather= weather
        self.__size = size
    
#Getters (métodos get)
    
    def get_name(self):
        return self.__name
    
    def get_color(self):
        return self.__color
    
    def get_shape(self):
        return self.__shape
    
    def get_taste(self):
        return self.__taste
    
    def get_weather(self):
        return self.__weather
    
    def get_size(self):
        return self.__size

# Setters (métodos set)
    
    def set_name(self,Newname):
        self.__name = Newname

    def set_color(self,Newcolor):
        self.__color = Newcolor
    
    def set_shape(self,Newshape):
        self.__shape = Newshape
    
    def set_taste(self,Newtaste):
        self.__taste = Newtaste

    def set_weather(self,Newweather):
        self.__weather = Newweather

    def set_size(self,Newsize):
        self.__size = Newsize
    
    def describir(self):
        print ('Soy el Padre')

#Clase hija 1
        
class hija_1(Fruit):
    def __init__(self, name,color,shape,taste,weather,size, scientificName, producingCountry,originative ):
# Llamada al constructor de la clase padre
        super().__init__(name,color,shape,taste,weather,size)
# Atributos propios de la clase hija 1
        self.__scientificName = scientificName
        self.__producingCountry = producingCountry
        self.__originative = originative

# Métodos get
    
    def get_scientificName(self):
        return self.__scientificName

    def get_producingCountry(self):
        return self.__producingCountry
        
    def get_originative (self):
        return self.__originative

# Métodos set
    
    def set_scientificName (self, newscientificName):
        self.__scientificName = newscientificName
        
    def set_producingCountry (self, newproducingCountry):
        self.__producingCountry = newproducingCountry
        
    def set_originative (self, neworiginative):
        self.__originative = neworiginative

def describir (self):
        print ('Soy la hija 1')

#Clase hija 2:

class hija_2(Fruit):
    def __init__(self, name, color, shape, taste, weather, size,weight,height,price):
# Llamada al constructor de la clase padre
        super().__init__(name, color, shape, taste, weather, size)

#Atributos propios de la clase hija 2:
    
        self.__weight = weight
        self.__height = height
        self.__price = price

# Métodos get

    def get_weigth(self):
        return self.__weight

    def get_height(self):
        return self.__height
        
    def get_price (self):
        return self.__price

 # Métodos set

    def set_weigth (self, newWeigth):
        self.__weight = newWeigth
        
    def set_height (self, newHeight):
        self.__height = newHeight
        
    def set_price (self, newPrice):
        self.__price = newPrice  
    
# Método adicional de llamado

    def describir (self):
        print ('Soy la hija 2')   










    
    

    
