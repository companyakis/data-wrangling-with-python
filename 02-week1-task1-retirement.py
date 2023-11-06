# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:34:59 2023

Task: Keep saving until you can retire.

Write a program to simulate how to save money for retirement.
1. Asks the user for a number representing a new positive deposit for the retirement fund.
2. Print out the amount of the deposit as well as the balance for each transaction.
3. When the balance is equal or more than 1 million, print a message "You can retire now" to
the user.
4. Print "Congratualtions!" and exit the program.

"""
total_amount = 0

while total_amount < 1000000:
    deposit = float(input("Deposit for the retirement fund: "))
    total_amount += deposit
    print("Deposit: ", deposit)
    print("Total amount: ", total_amount)

print("You can retire now.")
print("Congratualtions!")
