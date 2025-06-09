class BookStore:
    NoOfBooks = 0  # class variable
    
    def __init__(self):
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        self.Name = input("Enter Book Name: ")
        self.Author = input("Enter Author Name: ")
        
    def Display(self):
        print("Book Name: ",self.Name)
        print("Author Name: ",self.Author)
        print("No of Books: ",self.NoOfBooks)
    
    
    
def main():
    obj1 = BookStore()
    obj1.Display()
    obj2 = BookStore()
    obj2.Display()

if __name__ == "__main__":
    main()