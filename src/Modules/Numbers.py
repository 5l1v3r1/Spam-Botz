from Modules.Spammer import *
import time

def numbers():
    print("\n-----SEQUENTIAL NUMBERS SPAM-----")
    print("This is a spam method that sends numbers from 1 to n as seperate messages\n")
    try:
        count = int(input("Enter the number until which you want to spam \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(1,count+1):
        x = str(x)
        spammer(x,sleep)