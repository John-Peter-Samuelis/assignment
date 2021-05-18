def disemvoweler(str):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U')
    for alphabets in str:
        if alphabets in vowels:
            str = str.replace(" ", "")
            str = str.replace(alphabets, "")
    print(str, end=" ")


str = input("Enter String: ")
disemvoweler(str + " ")
for alphabets in str.lower():
    if alphabets in 'aeiouAEIOU':
        print(alphabets, end="")

