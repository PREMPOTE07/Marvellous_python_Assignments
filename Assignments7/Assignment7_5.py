def CheckPalindrome(str):
    List = []
    for i in range(len(str)):
        List.append(str[i])
    # check palindrome
    i = 0
    j = (len(List) - 1)
    while(i < j):
        if List[i] == List[j]:
            return True
        i += 1
        j -= 1
    return False
    
def main():
    str = input("Enter a string: ")
    if CheckPalindrome(str) == True:
         print("Palindrome")
    else:
         print("Not Palindrome")
    
if __name__ == "__main__":
    main()