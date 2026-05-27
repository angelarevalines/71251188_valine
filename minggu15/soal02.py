def palindrom(kata):
    kata = kata.lower().replace(" ", "")
    if len(kata) <= 1:
        return True
    return kata[0] == kata[-1] and palindrom(kata[1:-1])

#TESTCASE
print(palindrom("makam"))
print(palindrom("halloww"))
print(palindrom("yey"))