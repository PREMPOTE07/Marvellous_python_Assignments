def CalSum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def main():
    list= []
    
    size = int(input("How much number you want to insert: "))
    
    print("Enter the numbers: ")
    
    for i in range(size):
        no = int(input())
        list.append(no)
        
    result = CalSum(list)
    
    print("Sum is : ",result)

if __name__ == "__main__":
    main()