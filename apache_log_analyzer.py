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

#this opens our access log and assigns it to a variable after we read the contents of the log
logFile = open("m4-access.log","r")
apache_logs = logFile.read()

#next we split the log as you requested us not to use the readlines function in the assignment, that would shortcut this process by reading and spliting the lines in one process. 
apache_logs_split = apache_logs.split("\n")

#opening (will also create text file if it has not been created yet) apache_analysis.txt in preperation for the 'for' loop, using the "a" function to append our entries one at a time into the new txt file as the loop progresses.
newFile = open("apache_analysis.txt", "a")

#creating a 'for' loop to isolate each log entry for its ip address and HTTP return code, printing those values as they are split off from each line, and then appending each entry into a new file called apache_analysis.txt, and giving each entry its own line using \n.
for log in apache_logs_split:
    split_entries = log.split()
    isolated_ip_return_code = f"{split_entries[0]} - {split_entries[8]}"
    print(isolated_ip_return_code)
    newFile.write(f"{isolated_ip_return_code}\n")

#note I did not close the files as that was not stated in the assignment but normally I would at the end, trying to follow assignement to the letter.