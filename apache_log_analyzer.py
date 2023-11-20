#!/usr/bin/env python3
# Author: Alex Hickel 
# Email Address: ahickel@madisoncollege.edu 
# I use Word Wrap to make reading easier.
# Course Description: During the course project we will be adding new functionality to our scripts in order to process Apache Log entries. The Apache log entries comes from Apache web servers. We will summarize the data in the log to identitfy potential security threats, and deal with those threats by using different web services.

#importing the request, argparse, subprocess, and beautiful soup 4 modules to handle http requests, parse log entries, and use linux commands within our python script.
import requests, argparse, subprocess, bs4

#creating our IPLookup function to do a get request for our URL while using a formatted string to pass the arguement from the function into the url and then to pass our most popular IP address which will be a result from our IPAddressCount function into our new Lookup function while also printing the first 250 characters of the website at that url and pulling the beautiful soup HTML code from the HTML code to get information about the owner of the IP address printing it to the screen.
def IPLookup(IPAddress):
    response = requests.get(f"https://tools.keycdn.com/geo?host={IPAddress}")
    print(f"https://tools.keycdn.com/geo?host={IPAddress}")
    print(response.text[:250])
    myHTML = bs4.BeautifulSoup(response.text, features ="html.parser")
    print(myHTML.find_all("dd", class_="col-8 text-monospace")[1].text)

#creating a new function to run our bash shell script to parse the most common IP address from our Apache log file that is input as part of an arguement later on in our code. The function then splits the result of the most common IP address from that list, and returns the value of the most common one isolated to display only the IP address as the Isolated_IP value.
def IPAddressCount(apache_log_file_name):
    linux_process = subprocess.run(f"cat {apache_log_file_name}  | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n1",  shell=True, stdout=subprocess.PIPE)
    output = linux_process.stdout.decode()
    split_output = output.split('\n')
    split_output_list = split_output[0].split(' ')
    for IP in split_output_list:
        if '.' in IP:
            Isolated_IP = IP
    return Isolated_IP
    #newFile = open("apache_analysis.txt", "w")
    #newFile.write(output)
    #newFile.close()
    #print(output)

#putting our whole program into the main() function in order to be able to import functions we may want to use in another program
def main():

    #writing out our arguements for argparse, and storing them in the variable log to easily call the arguement input into our IPAddressCount function. Adding a required=true arguement to prevent the code from erroring if there is no arguement given.
    parser = argparse.ArgumentParser(description='A new parser for our script')
    parser.add_argument('-f', '--filename', dest='filename', type=str, required=True, help='Enter an Apache File Name to process')
    log = (parser.parse_args()).filename

    #This is the concise course description that I assigned to a variable
    CourseDescription= "Welcome! This program will help you to parse information from Apache Server Log entries to identify potential security threats so that you may deal with them accordingly."
    
    #print our course description before running our function
    print(CourseDescription)
    
   
    #storing our ioslated IP address from our IPAddressCount function which returns the most common IP address from our Apache Logs into a varible.
    IPAddress = IPAddressCount(log)
    
    #printing the isolated IP address which was returned from our IPAddressCount function.
    print(IPAddress)
    
    #calling our IPLookup function which is executing the code from above to provide us with the text from the URL and information about the IP address.
    IPLookup(IPAddress)

#this if statement checks if the main function is being imported or if the script is being run directly. If we were importing our script the __name__ would change to the name of the file and the main function would operate differently. Instead of executing the main() function in this case the body of the script, or main logic, it would effectively be able to then call the different functions and classes that were defined in the script instead of running the code contained within main().
if __name__ == "__main__":
    main()