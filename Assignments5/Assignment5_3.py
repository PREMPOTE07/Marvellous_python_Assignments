# vote eligibility checker
def voteEli(num):
    if num >= 18:
        return True
    return False

def main():
    no = int(input("Enter The Age: "))
    if voteEli(no) == True:
        print("Eligible For Vote")
    else:
        print("Not Eligible For Vote")
        
if __name__ == "__main__":
    main()