ConvertCToF = lambda c: (c * 9 / 5) + 32
    
def main():
    temp  = int(input("Enter the Temperature in Celcius: "))
    print("Temperature in Fahreniet is : ",ConvertCToF(temp),"F")
    
if __name__ == "__main__":
    main()