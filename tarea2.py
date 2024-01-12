#Clase persona

class persona:
    def __init__(self,firstName,lastName,age,gender,high,ocupattion):

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

        def get_padre(self):
            return 'Soy el Padre'
        
        