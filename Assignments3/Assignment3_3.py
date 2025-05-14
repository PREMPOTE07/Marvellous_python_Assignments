def CalMin(list):
    min = list[0]
    for i in range(1,len(list)):
        if (list[i] < min):
            min = list[i]
    return min

def main():
    list= []
    
    size = int(input("How much number you want to insert: "))
    
    print("Enter the numbers: ")
    
    for i in range(size):
        no = int(input())
        list.append(no)
        
    result = CalMin(list)
    
    print("Minimum in the list is : ",result)

if __name__ == "__main__":
    main()