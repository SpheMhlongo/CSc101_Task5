#!/usr/bin/python3

current_day = input("What is the starting day number? ")
stay_days = input("How long will your stay be? ")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

come_back_day = (int(current_day)+int(stay_days)) % 7

print("You will come back on day", come_back_day, "("+days[come_back_day]+")")