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