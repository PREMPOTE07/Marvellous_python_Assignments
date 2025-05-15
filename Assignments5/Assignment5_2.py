def CheckVowel(char):
    Characters = ['a','e','i','o','u']
    for i in range(len(Characters)):
        if char == Characters[i]:
            return True
    return False
def main():
   ch = input("Enter Any Character : ")
   if len(ch) == 1:
    if CheckVowel(ch) == True:
       print("'",ch,"'","is a Vowel")
    else:
       print("'",ch,"'","is a Consonant")
   else:
       print("Please Enter a single character")
if __name__ == "__main__":
    main()