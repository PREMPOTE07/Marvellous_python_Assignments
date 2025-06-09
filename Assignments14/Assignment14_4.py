class Student:
    school_name = "BVCOEL"
    
    def __init__(self,A,B):
        self.name = A
        self.rollNo = B
        
    def Display(self):
        print("School Name: ",Student.school_name)
        print("Student Name: ",self.name)
        print("Roll No: ",self.rollNo)
        
    def setSchoolName(self,A):
        Student.school_name = A
        
        
    
def main():
    Stud1 = Student("Prem",11)
    
    Stud1.Display()
    
    Stud1.setSchoolName("COEP")
    
    Stud1.Display()

if __name__ == "__main__":
    main()