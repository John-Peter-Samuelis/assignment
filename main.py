def disemvoweler(str):
    vowStore = ""
    consonantStore = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for alphabets in str:
        if alphabets in vowels:
            vowStore += alphabets
            vowStore = vowStore.replace(" ", "")
        else:
            consonantStore += alphabets
            consonantStore = consonantStore.replace(" ", "")
    print(consonantStore + " " + vowStore)


str = input("Enter String: ")
disemvoweler(str.lower())


