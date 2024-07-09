integer = int(input("Please enter a positive integer: "))
print("The factors of ",integer,"are:")
for num in range(1, integer+1):
    if integer % num == 0:
        print(num)
