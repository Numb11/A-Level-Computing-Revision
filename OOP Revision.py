class Employee:
    def __init__(self,role,name,birthd):

       salaries = {"President":70000,"Director":50000,"Manager":40000,"Scarer":35000,"Assistant":27000}
       self.salary = salaries[role]
       self.name = name
       self.email = f"{name.split()[0]}@MonsterInc.com"
       self.birthd = birthd
       self.useraccessl = "Lower"
       self.role = role
    def employee (self):
       return (self.name,self.email,self.birthd,self.salary,self.role,self.useraccessl)
   
class Corporate(Employee):
    def __init__(self,role,name,birthd):
        super().__init__(role,name,birthd)
        self.useraccessl = "Upper"
        self.email = f"{name.split()[0]}.corporate@MonsterInc.com"
    
        
sully = Employee("Scarer","Sully James","2000-08-17")
print(sully.employee())
mike = Corporate("President","Mike Wazowski","2000-08-17")
print(mike.employee())
