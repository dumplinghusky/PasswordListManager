import os
#import urllib2

list = []
names = []
temp_names = []
phoneNo = ''
dob = input("Date of birth(MMDDYYYY):")
if (len(dob) == 8):
    month = dob[:2]
    day = dob[2:4]
    year = dob[4:]
else:
    print("Wrong format for DOB, make sure it is 8 numbers in MMDDYYYY")
    exit()

phoneNo = input("Enter phone no:")


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
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)

def PostRun(WriteToFile,list):
    question = input("Do you want to merge with another wordlist on your computer? (Y/N)")
    if question == "N" or question == "n":
        WriteToFile(list)
    elif question == "Y" or question == "y":
        print("penis-aka still underdevelopment")
def mergewordlists(list):
    question = input("Merge with predefined wordlist?(requires internet)(Y/N)")
    if question == "N" or question == "n":
        PostRun(WriteToFile,list)
    elif question == "Y" or question == "y":
        print("Categories:")
        print("dogs,celebrities,holidays,food,tvmovies")
        urlquestion = input("What is this person interested in?")
        #data = urllib2.urlopen(target_url)

#things to add
#celebrities/athletes
#movies/music
#favorite animal/dogbreeds/cats
#importance-weighting
#foods
#wordlist merging

ListOfImportantWords()
for i in names:
    permute(i)
names = names + temp_names
WordListCreator(list)
mergewordlists(list)
