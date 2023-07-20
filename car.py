class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make 
        self.__speed = speed
                
        
        
        
    def accelerate(self):
        self.__speed += 5
        return self.__speed
    
    
    
    
    def brake(self):
        self.__speed -= 5
        return self.__speed
    
    
    
    
    def get_speed(self):
        return self.__speed
    
    
    
    
    def get_year_model(self):
        return self.__year_model
    
    
    
    
    def get_make(self):
        return self.__make
    
    
    
    
    def __str__(self):
        return f'Vehicle year: {self.__year_model}\n' \
        f'Vehicle make: {self.__make}\n' \
        f'Vehicle speed: {self.__speed} mph\n'
        