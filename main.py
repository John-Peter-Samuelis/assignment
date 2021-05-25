from itertools import permutations
listofCharacters = permutations(['a', 'b', 'c'], 2)

for eachCharacter in list(listofCharacters):
    print(''.join(eachCharacter), " ", end="")

