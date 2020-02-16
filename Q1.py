#!/usr/bin/python3

current_time = input("What time is it now (in hours)? ")
wait_time = input("How much time do you have wait for (in hours)? ")

time_in_24_format = (int(current_time)+int(wait_time)) % 24

if time_in_24_format >= 12:
	time_suffix = "pm"
else:
	time_suffix = "am"

print("Your alarm will ring at", str(time_in_24_format % 12) + time_suffix + ",", time_in_24_format)