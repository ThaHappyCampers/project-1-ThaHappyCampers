# project-2c

# Author: Joshua Garcia
# GitHun username: ThaHappyCampers
# Date: 7/1/2024
# Description: Write a program that asks the user for a (integer) number of cents, from 0-99
# and outputs how many of each type of coin would represent that amount with the fewest total number of coins.
print("Please enter an amount in cents less than a dollar.")
coins = int(input())
quarters = 25
dimes = 10
nickles = 5
pennies = 1

answer_1 = coins // quarters
remainder_1 = coins % quarters
answer_2 = remainder_1 // dimes
remainder_2 = coins % dimes
answer_3 = remainder_2 // nickles
remainder_3 = coins % nickles
answer_4 = remainder_3 // pennies

print("Your change will be:")
print("q:", answer_1)
print("d:", answer_2)
print("n:", answer_3)
print("p:", answer_4)
