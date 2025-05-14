def Search(list,searchNo):
    count = 0
    
    for i in range(len(list)):
        if list[i] == searchNo:
            count += 1
            
    if count == 0:
        print("The entered number is not in the list")
        
    return count

def main():
    list= []
    
    size = int(input("How much number you want to insert: "))
    
    print("Enter the numbers: ")
    
    for i in range(size):
        no = int(input())
        list.append(no)
    
    searchNo = int(input("Enter the number you want to search: "))
        
    result = Search(list,searchNo)
    
    print(searchNo,"is Entered in the list is : ",result," times")

if __name__ == "__main__":
    main()