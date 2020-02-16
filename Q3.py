#!/usr/bin/python3

P = 10000
n = 12
r = 8/100
t = int(input("Please enter the amount of years: "))

print("The final amount after", t, "days is", P*(1+r/n)**(n*t))
