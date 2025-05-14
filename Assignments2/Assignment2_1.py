import Arithmetic as A
def main():
    no1 = int(input("Enter First Number: "))
    no2= int(input("Enter Second Number: "))
    Artithmetic_name = {1: "Addition" , 2:"Subtraciton" , 3:"Multiplication" , 4: "Division"}
    set = {"1":A.Add(no1,no2) ,"2":A.Sub(no1,no2) ,"3":A.Mult(no1,no2) ,"4":A.Div(no1,no2) }
    print("Enter 1 For Addition / 2 For Subtraction / 3 For Multiplication / 4 For Division: ")
    no3 = int(input("Enter The Number: "))
    if no3 == 1:
        result = set["1"]
    elif no3 == 2:
        result = set["2"]
    elif no3 == 3:
        result = set["3"]
    elif no3 == 4:
       result = set["4"]
    else:
        print("invalid Number Please check condition")
    print(Artithmetic_name[no3] ,"is: ",result)
    
if __name__ == "__main__":
    main()