user = int(input("Enter height: "))
for i in range(user, 1, -1):
    print("*" * i)
for j in range(user-1):
    print("*" if j == 0 else " ", end="")
print("*")
for h in range(2,user+1):
    print("*"*h)
