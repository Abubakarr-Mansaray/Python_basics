#!/bin/python3

name = input("Enter your name: ")

age = int(input("Enter your age: "))

degree_program = input("Enter your degree program: ")



# Calculating remaining age

remaining_age = (age * 3) % 2



# Printing the message using string concatenation

print("Hello, my name is " + name + ", my remaining age is " + str(remaining_age) + ", and I am studying " + degree_program + " degree program.")


