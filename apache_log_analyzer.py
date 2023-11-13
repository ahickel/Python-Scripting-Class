#!/usr/bin/env python3
# Author: Alex Hickel 
# Email Address: ahickel@madisoncollege.edu 
# I use Word Wrap to make reading easier.
# Course Description: During the course project we will be adding new functionality to our scripts in order to process Apache Log entries. The Apache log entries comes from Apache web servers. We will summarize the data in the log to identitfy potential security threats, and deal with those threats by using different web services.

#Here I import the subprocess module so that I can run bash shell scripts within python
import subprocess

#importing argparse to use later in the program, this will help add arguements to executing my script
import argparse

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

    #writing out our arguements for argparse, and storing them in the variable log to easily call the arguement input into our IPAddressCount function.
    parser = argparse.ArgumentParser(description='A new parser for our script')
    parser.add_argument('-f', '--filename', dest='filename', type=str, help='Enter an Apache File Name to process')
    log = (parser.parse_args()).filename

    #This is the concise course description that I assigned to a variable
    CourseDescription= "Welcome! This program will help you to parse information from Apache Server Log entries to identify potential security threats so that you may deal with them accordingly."
    
    #print our course description before running our function
    print(CourseDescription)
    
    #calling our IPAddressCount function which is calling the arguement of our argparse command, in this case, the variable log which is our log input
    IPAddressCount(log)

#this if statement checks if the main function is being imported or if the script is being run directly. If we were importing our script the __name__ would change to the name of the file and the main function would operate differently. Instead of executing the main() function in this case the body of the script, or main logic, it would effectively be able to then call the different functions and classes that were defined in the script instead of running the code contained within main().
if __name__ == "__main__":
    main()