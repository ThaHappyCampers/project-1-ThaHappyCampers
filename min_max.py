# project-2c

# Author: Joshua Garcia
# GitHun username: ThaHappyCampers
# Date: 7/5/2024
# Description: Write a program that asks the user how many integers they would like to enter.

x = int(input("How many integers would you like to enter?"))
print("Please enter ", x," integers.")

first_v = input()
max = first_v
min = first_v
for num in range(1, x):
    second_v = input()
    if second_v > max:
        max = second_v
    if second_v < min:
        min = second_v
print("min: ", min)
print("max: ", max)
