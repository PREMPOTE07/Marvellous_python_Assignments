class Employee:
    def __init__(self,A,B,C):
        self.name = A
        self.emp_id = B
        self.salary = C
        
    def Display(self):
        print("Name: ",self.name)
        print("ID: ",self.emp_id)
        print("Salary: ",self.salary)
        
    
def main():
    emp1 = Employee("Rohit",101,50000)
    emp1.Display()

if __name__ == "__main__":
    main()