#!/usr/bin/env python3
# Author: Alex Hickel 
# Email Address: ahickel@madisoncollege.edu 
# I use Word Wrap to make reading easier.
# Course Description: During the course project we will be adding new functionality to our scripts in order to process Apache Log entries. The Apache log entries comes from Apache web servers. We will summarize the data in the log to identitfy potential security threats, and deal with those threats by using different web services.

#Here I import the subprocess module so that I can run bash shell scripts within python
import subprocess

#Here I use the import function to plug in, sys to use the commands to pass an arguement when I execute my file.
import sys

#creating a new function to run our bash shell script to parse the most common IP address from our Apache log file, and printing it to the screen, while also opening and writing the new IP information to our apache analysis.txt file.
def IPAddressCount(apache_log_file_name):
    linux_process = subprocess.run(f"cat {apache_log_file_name}  | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5",  shell=True, stdout=subprocess.PIPE)
    output = linux_process.stdout.decode()
    newFile = open("apache_analysis.txt", "w")
    newFile.write(output)
    newFile.close()
    print(output)

#putting our whole program into the main() function in order to be able to import functions we may want to use in another program
def main():

    #This is the concise course description that I assigned to a variable
    CourseDescription= "Welcome! This program will help you to parse information from Apache Server Log entries to identify potential security threats so that you may deal with them accordingly."

    #I set an if condition to see if someone is trying to pass an arguement, specifically "y" to bypass the input function. Prints the course description if they pass an acceptable arguement. 
    if len(sys.argv) > 1 and sys.argv[1] == "y":
        Continue = sys.argv[1]
        print(f"{CourseDescription}\n")

    #creating the else statement in case no arguement is passed, the program can continue.    
    else: 
        
        #printing the course description before the input statement and leaving a space.
        print(f"{CourseDescription} \n")
        
        #Setting up input sequence if there is no arguement to bypass it.
        Continue = input("Would you like to continue? Please reply with Y or N for yes or no.")
        
        #Printing the result of their successful input.
        print(f"\nThank you for your input, {Continue}\n")

    #If condition to pass their input through to verify if it's y, yeah, or yes.
    if Continue.lower() == "y" or Continue.lower() == "yeah" or Continue.lower() == "yes":
        
        #calling our bash shell function so that it runs within our script.
        IPAddressCount("m5-access.log")

    #Else statement stopping the program if the user inputs any value other than the assigned values to continue at the beginning.
    else:
        print("You choose not to continue.")

#this if statement checks if the main function is being imported or if the script is being run directly. If we were importing our script the __name__ would change to the name of the file and the main function would operate differently. Instead of executing the main() function in this case the body of the script, or main logic, it would effectively be able to then call the different functions and classes that were defined in the script instead of running the code contained within main().
if __name__ == "__main__":
    main()