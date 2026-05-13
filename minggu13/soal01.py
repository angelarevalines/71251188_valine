def persamaan(tuple):
    if len(tuple) == 0:
        return False
    for i in range(1, len(tuple)):
        if tuple[i] != tuple[0]:
            return False
    return True

print(persamaan((90,90,90,90)))
print(persamaan((90,88,90,90)))