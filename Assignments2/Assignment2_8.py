def pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j , end=" ")
        print()
def main():
    user_num = int(input("Enter the number: "))
    pattern(user_num)

if __name__ == "__main__":
    main()
    
