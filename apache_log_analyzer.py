#!/usr/bin/env python3
# Author: Alex Hickel 
# Email Address: ahickel@madisoncollege.edu 
# I use Word Wrap to make reading easier.
# Course Description: During the course project we will be adding new functionality to our scripts in order to process Apache Log entries. The Apache log entries comes from Apache web servers. We will summarize the data in the log to identitfy potential security threats, and deal with those threats by using different web services.

#defining our ParseLogEntry function which effectively pulls the IP address and the Return Code out of our line from our Apache Log Entry.
def ParseLogEntry(line):
    line_split = line.split()
    IP = line_split[0]
    return_code = line_split[8]
    return [IP,return_code]

#putting our whole program into the main() function in order to be able to import functions we may want to use in another program
def main():

    #This is the concise course description that I assigned to a variable
    CourseDescription= "Welcome! This program will help you to parse information from Apache Server Log entries to identify potential security threats so that you may deal with them accordingly."

    #Here I use the import function to plug in, sys to use the commands to pass an arguement when I execute my file.
    import sys

    #I set an if condition to see if someone is trying to pass an arguement, specifically "y" to bypass the input function.
    if len(sys.argv) > 1 and sys.argv[1] == "y":
        Continue = sys.argv[1]

    #creating the else statement in case no arguement is passed, the program can continue.    
    else: 
        #Setting up input sequence if there is no arguement to bypass it.
        Continue = input("Would you like to continue? Please reply with Y or N for yes or no.")
        #Printing the result of their successful input.
        print(f"Thank you for your input, {Continue}")

    #If condition to pass their input through to verify if it's y, yeah, or yes.
    if Continue.lower() == "y" or Continue.lower() == "yeah" or Continue.lower() == "yes":
        #Printing course description for this set.
        print(CourseDescription)
        
        #This opens our access log and assigns it to a variable after we read the contents of the log.
        logFile = open("m5-access.log","r")
        apache_logs = logFile.read()

        #Next we split the log as you requested us not to use the readlines function in the assignment, that would shortcut this process by reading and spliting the lines in one process. 
        apache_logs_split = apache_logs.split("\n")

        #Opening (will also create text file if it has not been created yet) apache_analysis.txt in preperation for the 'for' loop, using the "w" function to write our entries one at a time into the new txt file as the loop progresses.
        newFile = open("apache_analysis.txt", "w")

        #creating a dictionary for our IP addresses to be stored as keys. 
        apache_log_summary = dict()


        #Creating a 'for' loop to isolate each log entry for its ip address and HTTP return code, Then printing the return codes if they are 400 or greater as they are split off from each line. Also isolating the IP address by itself, and writing into the dictionary. For every additional pass of the same IP we will increase the stored value by 1 in the dictionary using an if statement.
        for log in apache_logs_split:

            #if int(split_entries[8]) >=500:
            #isolated_ip_return_code_large = f"{split_entries[0]} - {split_entries[8]}

            #assigning the function to a variable
            return_log = ParseLogEntry(log)
            
            #assigning the IP value from the function to the variable IP
            IP = return_log[0]
            
            #assigning the return code to a variable from the function
            return_code = return_log[1]

            #setting the keys from our dictionary to a variable
            IP_in_dict = apache_log_summary.keys()
            
            #checking if our IP we are parsing is in our dictionary already, and if so adding one to the total value of the pair to the IP key, otherwise the value just stays at 1 if it's the first time the IP is referenced in the dictionary.
            if IP in IP_in_dict:
                apache_log_summary[IP] += 1
            else:
                apache_log_summary[IP] = 1 
            
            #newFile.write(f"{isolated_ip_return_code_large}\n")
            if int(return_code) >=400:
                print(f"{IP} - {return_code}")
        
        #this for loop isolates only the IP address from the dictionary that are found more than, or equal to 5 times, and writes them to our analysis file.
        for key in apache_log_summary:
            if apache_log_summary[key] >= 5:
                newFile.write(f"{key} has {apache_log_summary[key]}\n")
        
        #Note I did not close the files as that was not stated in the assignment but normally I would at the end, trying to follow assignement to the letter.

    #Else statement stopping the program if the user inputs any value other than the assigned values to continue at the beginning.
    else:
        print("You choose not to continue.")

#this if statement checks if the main function is being imported or if the script is being run directly. If we were importing our script the __name__ would change to the name of the file and the main function would operate differently. Instead of executing the main() function in this case the body of the script, or main logic, it would effectively be able to then call the different functions and classes that were defined in the script instead of running the code contained within main().
if __name__ == "__main__":
    main()