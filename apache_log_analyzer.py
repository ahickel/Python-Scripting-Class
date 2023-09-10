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
