def pattern(num):
    for i in range(num):
        for j in range(num):
            print("*  " , end=" ")
        print()
def main():
    user_num = int(input("Enter the number: "))
    pattern(user_num)

if __name__ == "__main__":
    main()