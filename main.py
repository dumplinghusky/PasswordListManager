import os
# import urllib2

list = []
names = []
temp_names = []
phoneNo = ''
dob=''
month=''
day=''
year=''
bigboiwordlist = False
questioncheck = True
flags = ''
print("\n\n\n")
print(" __    __              _ _ _     _")
print("/ / /\ \ \___  _ __ __| | (_)___| |_    /\/\   __ _ _ __   __ _  __ _  ___ _ __")
print("\ \/  \/ / _ \| '__/ _` | | / __| __|  /    \ / _` | '_ \ / _` |/ _` |/ _ \ '__|")
print(" \  /\  / (_) | | | (_| | | \__ \ |_  / /\/\ \ (_| | | | | (_| | (_| |  __/ |")
print("  \/  \/ \___/|_|  \__,_|_|_|___/\__| \/    \/\__,_|_| |_|\__,_|\__, |\___|_|")
print("                                                                |___/         ")
print("\n\n\n")

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


def WordListCreator(list,bigboiwordlist):
    
    if bigboiwordlist == True:
        for word in names:
            #for i in range 0-length of word + 1
            for i in range(0, len(word) + 1):
                #add to list the word of to the i value plus birthday +
                list.append(word[:i] + day + word[i:])
                list.append(word[:i] + month + word[i:])
                #add word to the i value plus dob year 
                list.append(word[:i] + year + word[i:])
                #if the length of year is equal to four
                if len(year) == 4:
                    list.append(word[:i] + year[2:] + word[i:])
                list.append(word[:i] + phoneNo + word[i:])
        if not phoneNo == '':
            list.append(phoneNo)
    else:
        #for iterable word in names list
        for word in names:
            #for i in range 0-length of word + 1
            for i in range(0, len(word) + 1):
                #add to list the word of to the i value plus birthday +
                list.append(word[:i] + day + word[i:])
                list.append(word[:i] + month + word[i:])
                #add word to the i value plus dob year 
                list.append(word[:i] + year + word[i:])
                #if the length of year is equal to four
                if len(year) == 4:
                    list.append(word[:i] + year[2:] + word[i:])
                list.append(word[:i] + phoneNo + word[i:])
        if not phoneNo == '':
            list.append(phoneNo)
         


def WriteToFile(list):
    filename = input("enter a filename without the extension")
    with open(filename + '.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)
    print(filename + '.txt has been written to same path as main.py')
    questioncheck = True
    flag_questions(names,menu_select,questioncheck)



def mergewordlists(list):
    question = input("Merge with predefined wordlist?(requires internet)(Y/N)")
    if question == "N" or question == "n":
        PostRun(WriteToFile, list)
    elif question == "Y" or question == "y":
        print("still under development - errors ahead!")
        print("Categories:")
        print("dogs,celebrities,holidays,food,tvmovies")
        urlquestion = input("What is this person interested in?")
        # data = urllib2.urlopen(target_url)

    filename = input("enter a file name without extension")
    filename = filename + '.txt'
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


def menu_select(list,mergeexisting,mergewordlists):
    question = input(
        " Press 1 to merge with a wordlist on HD\n Press 2 to merge with predefined wordlist from repository(requires internet)\n Press 3 to write wordlist\n")
    question = int(question)
    if question == 1:
        mergeexisting(list)
    if question == 2:
        mergewordlists(list)
    if question == 3:
        WriteToFile(list)
    else:
        print("command not found try again")
        menu_select(list)


#def questions():
#    global year, dob, phoneNo, month, day
#    dob = input("Target date of birth(MMDDYYYY):")
#   if (len(dob) == 8):
#      day = dob[2:4]
#        year = dob[4:]
#    else:
#        print("Wrong format for DOB, make sure it is in format MMDDYYYY")
#        exit()
#    phoneNo = input("Enter phone no:")
#    return dob, phoneNo, month, day, year


def flag_questions(names,menu_select,questioncheck):
    global year, dob, phoneNo, month, day, bigboiwordlist, areacode, last_four,mergeexisting,mergewordlists, flags
    donecheck = False
    while questioncheck == True:
        flags = input("Enter command flags to create or manage wordlists, h for help \n\n\n")
        questioncheck = False
        flag_questions(names,menu_select,questioncheck)
    if flags == '':
        exit()
    if 'a' in flags:
        flags = '-xpfmsgwc'
        donecheck = True
    if '-x' in flags:
        bigboiwordlist = True
    if "p" in flags:
        num_pets = input('how many pets?\n')
        if int(num_pets) == 0:
            flags = '-xfmsgwc'
            questioncheck = False
        else:
            for i in range(int(num_pets)):
                names.append(input('pet name:\n'))
                donecheck = True
        
    if 'f' in flags:
        names.append(input('Childs name:\n'))
        names.append(input("Childs nickname:\n"))
        names.append(input("Partners name:\n"))
        names.append(input("Partners Nickname:\n"))
        donecheck = True
    if 'm' in flags:
        names.append(input("Favorite Celebrities/Athletes:\n"))
        names.append(input("Favorite movie/tv show:\n"))
        donecheck = True
    if 's' in flags:
        names.append('!')
        names.append('@')
        names.append('$')
        names.append('*')
        names.append(input("!,@,$,* added - any additional? (blank to continue)"))
    if 'g' in flags:
        phoneNo = input("Enter phone no:(no countrycode)\n")
        if (len(phoneNo)) == 10:
            areacode = phoneNo[:3]
            last_four = phoneNo[6:]
            
        dob = input("Target date of birth(MMDDYYYY):\n")
        if (len(dob) == 8):
            month = dob[:2]
            day = dob[2:4]
            year = dob[4:]
        else:
            print("Wrong format for DOB, make sure it is in format MMDDYYYY")
            print("Sending back to main menu")
            flag_questions(names,menu_select,questioncheck)
        names.append(input("Current City:\n"))
        names.append(input("Country:\n"))
        names.append(input("Favourite color:\n"))
        names.append(input("Nickname:\n"))
        names.append(input("ZipCode"))
        donecheck = True
    if 'w' in flags:
        names.append(input("Company/School name:\n"))
        donecheck = True
    if 'c' in flags:
        print("Enter all other keywords: \n")
        while True:
            inp = input()
            if inp == '':
                break
            names.append(inp)
        donecheck = True
    if 'h' in flags:
        print("select the attributes that apply to target\n Using a or g recommended")
        print("flags: p-pet, f-family, m-media, s-symbol, g-general, w-work/school, c-custom, a - full selection(no symbols)\n z - skip to management , blank to exit")
        print("***TO TURN ON COMPLEX WORDLISTS USE '-x'***")
        print("for example, pfc -x - sets profile flags for (P)et (F)amily (C)ustom and complex wordlists")
        print("A - sets all profile flags")
        print("at least 3 flags recommended")
        print("")
        flag_questions(names,menu_select,questioncheck)
        donecheck = True
    if 'z' in flags:
        location = input("location of wordlists to manage?")
        files = os.listdir(location)
        for f in files:
            print(f)
    if donecheck == True:
        startPermute(names, temp_names)
        WordListCreator(list,bigboiwordlist)
        menu_select(list,mergeexisting,mergewordlists)
        while ('' in names):
                names.remove('')
        
        #with open(location + '.txt', 'w') as f:
        #for item in list:
        #    f.write("%s\n" % item)
        #for line in file:
    else:
        print("Command not recognized")
        print("try again")
        flag_questions(names,menu_select,questioncheck)
        
        
# cleans out '' from names list

    return dob, phoneNo, month, day, year,

def startPermute(names, temp_names):
    for i in names:
        permute(i)
    names = names + temp_names
   



# things to add

# importance-weighting
# foods
# wordlist merging
# wildcards

def run():
    #questions()
    flag_questions(names,menu_select,questioncheck)
    # ListOfImportantWords()
    
run()


