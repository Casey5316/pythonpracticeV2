class Employee:
    def __init__(self, name, number):
        self.__employee_name = name
        self.__employee_num = number 
        
        
        
    def set_name(self, name):
        self.__employee_name = name
        
        
        
    def set_number(self, number):
        self.__employee_num = number
        
        
        
    def get_name(self):
        return self.__employee_name
    
    
    
    def get_number(self):
        return self.__employee_num
    
    
    
    def __str__(self):
        return f'Employee name: {self.__employee_name}\nEmployee number: {self.__employee_num}'
    
    
    
    
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_no, wage):
        Employee.__init__(self, name, number)
        
        self.__shift_no = shift_no
        self.__wage = wage
        
        
        
        
    def set_shift_no(self, shift_no):
        self.__shift_no = shift_no
        
        
        
        
    def set_wage(self, wage):
        self.__wage = wage
        
        
        
        
    def get_shift_no(self):
        return self.__shift_no
    
    
    
    
    def get_wage(self):
        return self.__wage
    
    
    
    
class ShiftSupervisor(Employee):
    def __init__(self, name, number, salary, prod_bonus):
        self.__name = name
        self.__number = number
        self.__salary = salary 
        self.__bonus = prod_bonus
        
        
        
        
    def set_salary(self, salary):
        self.__salary = salary
        
        
        
        
    def set_bonus(self, prod_bonus):
        self.__bonus = bonus
        
        
        
        
    def get_salary(self):
        return self.__salary
    
    
    
    def get_bonus(self):
        return self.__bonus