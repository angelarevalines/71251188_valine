def prima(n, bagi = 2):
    if n < 2:
        return False
    if bagi > n ** 0.5:
        return True
    if n % bagi == 0:
        return False
    return prima(n, bagi + 1)

#TEST CASE
print(prima(5))
print(prima(20))
print(prima(11))