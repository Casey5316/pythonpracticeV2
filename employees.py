class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        
        
        
        
    def set_name(self, name):
        self.__name = name
        
        
        
        
    def set_number(self, number):
        self.__number = number 
        
        
        
        
    def get_name(self):
        return self.__name
    
    
    
    
    def get_number(self):
        return self.__number
    
    
    
    
    def __str__(self):
        return f'Employee name: {self.__name}\nEmployee number: {self.__number}'
    
    
    
    
    
    

    
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number)
        
        self.__shift = shift
        self.__pay = pay
        
        
        
        
    def set_shift(self, shift):
        self.__shift = shift
        
        
        
        
    def set_pay(self, pay):
        self.__pay = pay
        
        
        
        
    def get_shift(self):
        return self.__shift
    
    
    
    
    def get_pay(self):
        return self.__pay
    
    
    
    
    
    
    
    
    
class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, bonus):
        Employee.__init__(self, name, number)
        
        self.__annual_salary = annual_salary
        self.__bonus = bonus
        
        
        
        
    def set_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        
        
        
        
    def set_bonus(self, bonus):
        self.bonus = bonus
        
        
        
        
    def get_salary(self):
        return self.__annual_salary
    
    
    
    
    def get_bonus(self):
        return self.__bonus