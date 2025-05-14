def pattern(num):
    for i in range(1,num):
        for j in range(1,num):
            print(j , end=" ")
        print()
def main():
    user_num = int(input("Enter the number: "))
    pattern(user_num)

if __name__ == "__main__":
    main()
    
