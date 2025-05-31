
def main():
    char = input("Enter a charecter : ")
    
    if char in "aeiouAEIOU":
        print(char,"is a vowel")
    else:
        print(char,"is a consonant")

if __name__ == "__main__":
    main()