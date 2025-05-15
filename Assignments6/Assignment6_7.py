def Greatest(list):
    gtr = 0
    for i in list:
        if i > gtr:
            gtr = i
    return gtr
        
        
def main():
    list = []
    print("Enter the 5 numbers: ")
    for i in range(5):
        no = int(input())
        list.append(no)
        
    result = Greatest(list)
    print("Greatest Element: ",result)
    
if __name__ == "__main__":
    main()
        
        