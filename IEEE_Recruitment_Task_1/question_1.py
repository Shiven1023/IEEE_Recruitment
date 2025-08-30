n = int(input("Enter number of rows in the pattern: "))
for i in range(n):
    print(" "*(n-i+1) + "*"*(i+1))