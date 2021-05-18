def disemvoweler(str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for alphabets in str.lower():
        if alphabets in vowels:
            for letters in str.lower():
                if letters in vowels:
                    str = str.replace(" ", "")
                    str = str.replace(letters, "")
            print (str + " ",(alphabets))


str = input("String: ")
disemvoweler(str)