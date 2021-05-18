def disemvoweler (str):
    vowels = ('a','e','i','o','u')
    storeVw = ""
    for alphabets in str:
        if alphabets in vowels:
            storeVw += alphabets
            str = str.replace(" ", "")
            str = str.replace(alphabets, "")
    print (str + " " + storeVw)

str = input("Enter String: ")
disemvoweler(str)
