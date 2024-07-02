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

answer_1 = (coins // quarters)
# 87 / 25 = 3
remainder_1 = (coins % quarters)
# 87 / 25 = 12(R1)

answer_2 = (remainder_1 // dimes)
# 12(R1) / 10 = 1
remainder_2 = (remainder_1 % dimes)
# 12 / 10 = 1(R2)

answer_3 = (remainder_2 // nickles)
# 7(R2) / 5 = 1
remainder_3 = (remainder_2 % nickles)
# 2 / 5 = 0(R2)

answer_4 = (remainder_3 // pennies)
# 2(R3) / 1 = 2

print("Your change will be:")
print("Q:", answer_1)
print("D:", answer_2)
print("N:", answer_3)
print("P:", answer_4)
