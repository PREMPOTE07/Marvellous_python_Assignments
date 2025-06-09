class Employee:
    def __init__(self,A,B,C):
        self.name = A
        self._department = B # protected
        self.__salary = C    # private
    
    def Display(self):
        print("Name: ",self.name)
        print("Department: ",self._department)
        print("Salary: ",self.__salary)
                
def main():
    emp1 = Employee("Prem","Associ",35000)
    emp2 = Employee("Niranjan","HR",67000)
    
    emp1.Display()
    emp2.Display() 
    
    
    emp1.__salary = 25000    # cant change or access because private 
    
    emp1.Display()

if __name__ == "__main__":
    main()