def CalMax(list):
    max = 0
    for i in range(len(list)):
        if (list[i] > max):
            max = list[i]
    return max

def main():
    list= []
    
    size = int(input("How much number you want to insert: "))
    
    print("Enter the numbers: ")
    
    for i in range(size):
        no = int(input())
        list.append(no)
        
    result = CalMax(list)
    
    print("Maximum in the list is : ",result)

if __name__ == "__main__":
    main()