import os
#import urllib2

list = []
names = []
temp_names = []
phoneNo = ''


print(" __    __              _ _ _     _")
print("/ / /\ \ \___  _ __ __| | (_)___| |_    /\/\   __ _ _ __   __ _  __ _  ___ _ __")
print("\ \/  \/ / _ \| '__/ _` | | / __| __|  /    \ / _` | '_ \ / _` |/ _` |/ _ \ '__|")
print(" \  /\  / (_) | | | (_| | | \__ \ |_  / /\/\ \ (_| | | | | (_| | (_| |  __/ |")
print("  \/  \/ \___/|_|  \__,_|_|_|___/\__| \/    \/\__,_|_| |_|\__,_|\__, |\___|_|")
print("                                                                |___/         ")



def ListOfImportantWords():
    names.append(input("First name:"))
    names.append(input("Last Name:"))
    names.append(input("Nickname:"))
    print("\n")
    names.append(input("Partners name:"))
    names.append(input("Partners Nickname:"))
    print("\n")
    names.append(input("Pets name:"))
    names.append(input("Company/School name:"))
    print("\n")
    names.append(input("Childs name:"))
    names.append(input("Childs nickname:"))
    print("\n")
    names.append(input("City:"))
    names.append(input("Country:"))
    names.append(input("Favourite color:"))
    print("\n")
    names.append(input("Favorite Celebrities/Athletes:"))
    print("Enter all other keywords: ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)
    while ('' in names):
        names.remove('')


def permute(inp):
    n = len(inp)

    mx = 1 << n

    inp = inp.lower()

    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()

        temp = ""
        for i in combination:
            temp += i
        temp_names.append(temp)


def WordListCreator(list):
    for word in names:
        for i in range(0, len(word) + 1):
            list.append(word[:i] + day + word[i:])
            list.append(word[:i] + month + word[i:])
            list.append(word[:i] + year + word[i:])
            if len(year) == 4:
                list.append(word[:i] + year[2:] + word[i:])
            list.append(word[:i] + phoneNo + word[i:])
    if not phoneNo == '':
        list.append(phoneNo)


def WriteToFile(list):
    filename = input("enter a filename without the extension")
    filename.append(".txt")
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)

def PostRun(WriteToFile,list):
    question = input("Do you want to merge with another wordlist on your computer? (Y/N)")
    if question == "N" or question == "n":
        WriteToFile(list)
    elif question == "Y" or question == "y":
        print("still underdevelopment")
def mergewordlists(list):
    question = input("Merge with predefined wordlist?(requires internet)(Y/N)")
    if question == "N" or question == "n":
        PostRun(WriteToFile,list)
    elif question == "Y" or question == "y":
        print("Categories:")
        print("dogs,celebrities,holidays,food,tvmovies")
        urlquestion = input("What is this person interested in?")
        #data = urllib2.urlopen(target_url)

    filename = input("enter a file name without extension")
    filename.append(".txt")
    with open(filename, 'w') as f:
        for item in list:
            f.write("%s\n" % item)

    def mergeexisting(list):
        print("still under development")


def mergewordlists(list):
        print("Categories:")
        print("dogs,celebrities,holidays,food,tvmovies")
        urlquestion = input("What is this person interested in?")
        # data = urllib2.urlopen(target_url)


def menu_select(list):
    question = input(" Press 1 to merge with a wordlist on HD\n Press 2 to merge with predefined wordlist from repository(requires internet)\n Press 3 to write wordlist.txt")
    if question == 1:
        mergeexisting(list)
    elif question == 2:
        mergewordlists(list)
    elif question == 3:
        WriteToFile(list)
    else:
        print("command not found try again")
        menu_select(list)


def questions():
    global year, dob, phoneNo, month, day
    dob = input("Date of birth(MMDDYYYY):")
    if (len(dob) == 8):
        month = dob[:2]
        day = dob[2:4]
        year = dob[4:]
    else:
        print("Wrong format for DOB, make sure it is in format MMDDYYYY")
        exit()
    phoneNo = input("Enter phone no:")
    return dob, phoneNo, month, day, year

#things to add
#celebrities/athletes
#movies/music
#favorite animal/dogbreeds/cats
#importance-weighting
#foods
#wordlist merging

questions()


ListOfImportantWords()
for i in names:
    permute(i)
names = names + temp_names


WordListCreator(list)
menu_select(list)

