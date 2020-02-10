import time
import datetime
hosts_temp=r"C:\Users\RMAda\PycharmProjects\PythonMEGACourse2\hosts" #Using this temporarily as will need to run cmd as administrator when program is ready
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #Need to add r
redirect="127.0.0.1" #This is the local address of the unable to connect page
website_list=["wwww.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

from datetime import datetime as dt

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17): #This is comparing current time with the defined working hours (8-17)
        print("Working Hours")
        with open(hosts_temp, 'r+') as file: #reads the hosts file into python. r+ is read and append
            content=file.read()
            print(content)
            for website in website_list: # iterates through the list of websites to see if they are in the host file
                if website in content:
                    pass # do nothing if the website is already in the host file
                else:
                    file.write(redirect + " " + website + "\n") #Adds the list of forbidden websites to the host file with the local redirect address "\n" adds a new line after each
    else:
        print("Time to play")
        with open(hosts_temp, 'r+') as file: #reads the hosts file into python. r+ is read and append - will add content to the bottom
            content=file.readlines() #Reads the file as a list
            file.seek(0) #Moves pointer to the start
            for line in content:
                if not any(website in line for website in website_list): #Checks each line to see if the list items are present. If they are not then the line is written
                    file.write(line) #This writes the line. Esentially re-writing the whole file without the items from the website list. This creates a lot of extra lines underneath which need deleting.
                file.truncate() #Deletes the previous host text, which has now been replaced
    time.sleep(5)