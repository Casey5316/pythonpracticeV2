class Pet:
    
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__type = animal_type
        self.__age = age
        
        
        
    
    def set_name(self, name):
        self.__name = name
        
        
        
        
    def set_type(self, animal_type):
        self.__type = animal_type
        
        
        
        
    def set_age(self, age):
        self.__age = age
        
        
        
        
    def get_name(self):
        return self.__name
    
    
    
    
    def get_type(self):
        return self.__type
    
    
    
    
    def get_age(self):
        return self.__age
    
    
    
    def __str__(self):
        return f'{self.__name} is a {self.__age} year old {self.__type}'