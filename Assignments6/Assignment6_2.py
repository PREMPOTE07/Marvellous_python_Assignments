def main():
    sum = 0
    # for i in range(1,101):
    #     if i % 2 == 0:
    #         sum += i
    # print("Sum of Even Numbers Between 1 and 100: ",sum)
    
    # using while loop 
    i = 0
    while(i < 101):
        if i % 2 == 0:
            sum += i
        i += 1
        
    print("Sum of Even Numbers Between 1 and 100: ",sum)
    
if __name__ == "__main__":
    main()