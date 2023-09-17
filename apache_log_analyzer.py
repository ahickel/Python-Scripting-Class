#!/usr/bin/env python3
# Author: Alex Hickel 
# Email Address: ahickel@madisoncollege.edu 
# I use Word Wrap to make reading easier.
# Course Description: During the course project we will be adding new functionality to our scripts in order to process Apache Log entries. The Apache log entries comes from Apache web servers. We will summarize the data in the log to identitfy potential security threats, and deal with those threats by using different web services.

#This is the concise course description that I assigned to a variable
CourseDescription= "Welcome! This program will help you to parse information from Apache Server Log entries to identify potential security threats so that you may deal with them accordingly."

#This prints the variable containing the shortened course description
print(CourseDescription)

#Here I assign the user's input to the variable Continue
Continue = input("Would you like to continue? Please reply with Y or N for yes or no.")

#This line prints for the user a recognition that their entry was received
print(f"Thank you for your input, {Continue}")

#converting apache log info into a string and attaching it to a variable
apache_log_address = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'

#Slice code to isolate IP address from the beginning of the string, and print it
slice_ip = apache_log_address[0:15]
print(f"Log request from:{slice_ip:*^22}")

#Using split function to print the return code value from the apache log string
split_log = apache_log_address.split()
print(f"Return Code: {split_log[8]}")