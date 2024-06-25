row = int(input("Enter row: "))
col = int(input("Enter col: "))
i = 1

while i <= row:
    j = 1
    while j <= col:
        if i == 1 or j == 1 or i == row or j == col:
            print("*", end="")
        else:
            print(" ", end="")
        j+=1
    i+=1
    print("")
    