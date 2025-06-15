size = int(input("Enter the size of the pattern: "))
i = 0
j = 0
while i < size:
    for j in range(size):
        print("*", end="")
        j += 1
    print()
    i += 1