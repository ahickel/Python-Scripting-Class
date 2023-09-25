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
#Continue = input("Would you like to continue? Please reply with Y or N for yes or no.")

#This line prints for the user a recognition that their entry was received
#print(f"Thank you for your input, {Continue}")

#converting apache log info into a single string, while making sure to add in new lines using \n for each entry, and attaching the log entries to a single variable.
apache_logs ='111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" \n111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" \n111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)" \n111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'

#This code converts each log entry into a list, using the split function, by seperating each entry with the \n break.
seperated_log_list = apache_logs.split("\n")

#creating a 'for' loop to isolate each log entry while also slicing code to print the isolated IP address from the beginning of the string. We're also using split function to print the return code value from the isolated apache log string, which has been converted into a list within the loop.
for log in seperated_log_list:
    slice_ip = log[0:15]
    print(f"Log request from: {slice_ip:*^22}")
    split_log = log.split()
    print(f"Return Code: {split_log[8]}")