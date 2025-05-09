def Display_len(name):
    name_without_space = name.replace(" ","") # without space function
    print(len(name_without_space)) # print without space
    print(len(name)) # print with space
      
        
def main():
  Display_len("Prem")
  Display_len("Marvellous Infosystems")
 
      
    
if __name__ == "__main__":
    main()