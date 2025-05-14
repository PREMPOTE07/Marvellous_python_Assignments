import MarvellousNum as M
def ListPrime(list):
    sum = 0
    
    for i in range(len(list)):
        if(M.ChkPrime(list[i])):
            sum += list[i]
            
    return sum

def main():
    list= []
    
    size = int(input("How much number you want to insert: "))
    
    print("Enter the numbers: ")
    
    for i in range(size):
        no = int(input())
        list.append(no)
    
        
    result = ListPrime(list)
    
    print("Sum of Prime Number in the list are : ",result)

if __name__ == "__main__":
    main()
