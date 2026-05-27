def kombinasi(n, k):
    if k == 0 or k == n:
        return 1
    return kombinasi(n - 1, k - 1) + kombinasi(n - 1, k)

#TESTCASE
print(kombinasi(7, 5))
print(kombinasi(12, 9))
print(kombinasi(23, 7))

