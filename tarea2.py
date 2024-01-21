#Clase persona

class persona:
    def __init__(self, firstName, lastName, age, gender, high, ocupattion):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__gender = gender
        self.__high = high
        self.__ocupattion = ocupattion
        

    # Getters (métodos get)

    def get_name(self):
            return self.__firstName
        
    def get_lastName(self):
            return self.__lastName
        
    def get_age(self):
            return self.__age
        
    def get_gender(self):
            return self.__gender
        
    def get_high(self):
            return self.__high
        
    def get_ocupattion(self):
        return self.__ocupattion
        

# Setters (métodos set)
        
    def set_name(self, newName):
        self.__firstName = newName

    def set_lastName(self, newlastName):
        self.__lastName = newlastName
        
    def set_age(self, newAge):
        self.__age = newAge
    
    def set_gender(self, newGender):
        self.__gender = newGender

    def set_high(self, newHigh):
        self.__high = newHigh
        
    def set_ocupattion(self, newOcupattion):
        self.__ocupattion = newOcupattion

    def describir(self):
        print ('Soy el Padre')
        

#Clase hija 1

class hija_1(persona):
    def __init__(self,nickName,hobbie,motherName,firstName,lastName,age,gender,high,ocupattion):
         # Llamada al constructor de la clase padre
        super().__init__(firstName,lastName,age,gender,high,ocupattion)
         # Atributos propios de la clase hija 1
        
        self.__nickName = nickName
        self.__hobbie = hobbie
        self.__motherName = motherName

        # Métodos set

    def set_nickName (self, newNickName):
        self.__nickName = newNickName
        
    def set_hobbie (self, newHobbie):
        self.__hobbie = newHobbie
        
    def set_motherName (self, newMotherName):
        self.__motherName = newMotherName
        
        # Métodos get
        
    def get_nickName(self):
        return self.__nickName

    def get_hobbie(self):
        return self.__hobbie
        
    def get_motherName (self):
        return self.__motherName
        
        # Método adicional de llamado

    def describir (self):
        print ('Soy la hija 1')


#Clase hija 2:

class hija_2(persona):
    def __init__(self,nacionality,favoriteFood,favoriteColor,firstName,lastName,age,gender,high,ocupattion):
         # Llamada al constructor de la clase padre
        super().__init__(firstName,lastName,age,gender,high,ocupattion)
        
         # Atributos propios de la clase hija 2
        
        self.__nacionality = nacionality
        self.__favoriteFood = favoriteFood
        self.__favoriteColor = favoriteColor

        # Métodos set

    def set_nacionality (self, newNacionality):
        self.__nacionality = newNacionality
        
    def set_favoriteFood (self, newFavoriteFood):
        self.__favoriteFood = newFavoriteFood
        
    def set_favoriteColor (self, newFavoriteColor):
        self.__favoriteColor = newFavoriteColor
        
     # Métodos get
        
    def get_nacionality(self):
        return self.__nacionality

    def get_favoriteFood(self):
        return self.__favoriteFood
        
    def get_favoriteColor (self):
        return self.__favoriteColor
        
    # Método adicional de llamado

    def describir (self):
        print ('Soy la hija 2')
    

persona1 = persona("Marcos","Perez",27,"M",180,"Estudiante")
print(persona1.get_name())
persona1.describir()

persona2 = hija_1("nickName","hobbie","motherName","firstName","lastName",30,"F",180,"ocupattion")
print(persona2.get_nickName())
persona2.describir()


persona3 = hija_2("nacionality","favoriteFood","favoriteColor","firstName","lastName",25,"M",180,"ocupattion")
print(persona3.get_nacionality())
persona3.describir()




        
        
    

        



        
        