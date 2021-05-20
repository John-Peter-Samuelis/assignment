transform = (input("Enter a word: "))
if any(s.isdigit() for s in transform):
    raise ValueError("input should be of type 'str'")

transform = transform.lower()
if transform[0] in "bcdfghjklmnpqrstvwxyz":
    print("Original Word:", transform)
    print("Transformed Word:", transform[1:] + transform[0] + "ay")
else:
    print ("Does not recognise word")
