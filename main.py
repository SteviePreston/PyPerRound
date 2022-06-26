from functions.functions import *
from datetime import date
from nis import match
from time import sleep
import os

print("Good Morning Stevie!, Todays date is: ", date.today())
sleep(5)

print("Here is the news!")
sleep(5)

menu = "N - [News] - Daily Mail | T - [Tech] -  BBC Technology | B - [Buisness] - Wall Street Journal | C - [Crypto] - Nasdaq Crypto | A - [AI] - Nasdaq Artifical Intelligence | R - [Reset] - Reset Terminal | Q - [Quit]"
end = "=============================================================================="

def fetchNews(usrInputNews):
    match usrInputNews:
        case "n"  "N":
            getDailyMail()
            print(end)
            print(menu)

        case "t" "T":
            getBBCTech()
            print(end)
            print(menu)

        case "b" "B":
            getWallStJournal()
            print(end)
            print(menu)

        case "c" "C":
            getNasdaqCrypto()
            print(end)
            print(menu)

        case "a" "A":
            getNasdaqAI()
            print(end)
            print(menu)

        case "r" "R":
            os.clear()
            print(menu)
            
        case "q" "Q":
            os.clear()

        case _:
            return menu


usrInputNews = input()
fetchNews()

print("What are we working on today?")

usrInput = input()

workmenu = "C - [C] | P - [Python] | R - [React] | N - [Node] | A - [Artifical Intelligence | J - [Java] | B - [Bash] | Q - [Quit]"

def startWork(usrInput):
    match usrInput:
        case "c" "C":
            ChDir2c()
            os.system("code .")

        case "p" "P":
            ChDir2py()
            os.system("code .")

        case "r" "R":
            ChDir2react()
            os.system("code .")

        case "n" "N":
            ChDir2node()
            os.system("code .")

        case "a" "A":
            ChDir2ai()
            os.system("code .")

        case "j" "J":
            ChDir2java()
            os.system("code .")

        case "q" "Q":
            os.clear()
            print("Enjoy your day!")

        case _:
            print("C - [C] | P - [Python] | R - [React] | N - [Node] | A - [Artifical Intelligence | J - [Java] | B - [Bash]")




print("Happy Hacking!")