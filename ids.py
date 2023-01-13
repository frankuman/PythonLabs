#Hur lång tid trodde du det skulle ta? Total arbetstid kanske 24h
#Hur lång tid tog det? Cirka 8h



import os
import hashlib

def find_subdirs(directory): #Carina föreläsning inför lab 4

    sub_dirs = []
    paths = os.listdir(directory)
    for path in paths: 
        fullpath = directory +  '/' + path
        if os.path.isdir(fullpath):
            sub_dirs.append(fullpath)
            sub_dirs += find_subdirs(fullpath)

    return sub_dirs


def find_subfiles(directory):
    sub_files = []

    paths = os.listdir(directory)
    for files in paths:
        fullpath = directory +  '/' + files

        if os.path.isfile(fullpath):
            sub_files.append(fullpath)

        if os.path.isdir(fullpath):
            sub_files += find_subfiles(fullpath)

    return sub_files

def print_found(sub_dirs, sub_files):
    if len(sub_dirs) == 0:
        print("No other directory found")
    if len(sub_dirs) > 0:
        print("Found other directories")
    if len(sub_files) == 0:
        print("No other files found")
    if len(sub_dirs) > 0:
        print("Found other files")

def binary_creator(sub_files):
    binary_list = []
    for line in sub_files:
        f = open(line, "rb")
        binary = f.read()
        binary_list.append(binary)
        f.close()

    return binary_list

def hasher(binary_list):
    hashed_list = []

    for lines in binary_list:
        m = hashlib.sha256()
        m.update(lines)
        m = m.hexdigest()
        hashed_list.append(m)
    return hashed_list

def checker(hashed_list, binary_list, directory, sub_files, sub_dirs):
    try:
        report = str(input("Type Report to do a report, type Menu to go back: "))
        report = report.lower()
    except EOFError:
        report = 'report'
        
    if not os.path.isdir(directory):
        print("WARNING: EVERYTHING WAS DELETED OR THE FOLDER CHANGED NAME")
        print("\n------------------")
        main()

    if report == 'report':
        print("\n")
        check_sub_dirs = find_subdirs(directory)
        check_sub_files = find_subfiles(directory)
        check_binary_list = binary_creator(check_sub_files)
        check_hashed_list = hasher(check_binary_list)

        if check_sub_dirs != sub_dirs:
                for n ,something in enumerate(sub_dirs):
                    if sub_dirs[n] not in check_sub_dirs:
                        print("REMOVED")
                        print(sub_dirs[n])
    
                        print("\n --------------------")
                for n ,something in enumerate(check_sub_dirs):
                    if check_sub_dirs[n] not in sub_dirs:
                        print("NEW")
                        print(check_sub_dirs[n])
   
   
                        print("\n --------------------")


        if check_sub_files != sub_files:
                for n ,something in enumerate(sub_files):
                    if sub_files[n] not in check_sub_files:
                        print("REMOVED")
                        print(sub_files[n])

                        print("\n --------------------")
                for n ,something in enumerate(check_sub_files):
                    if check_sub_files[n] not in sub_files:
                        print("NEW")
                        print(check_sub_files[n])
                        print("\n --------------------")

        if check_hashed_list != hashed_list:
            for n ,something in enumerate(hashed_list):
                try:
                    if hashed_list[n] not in check_hashed_list and sub_files[n] in check_sub_files:
                        print("CHANGED FILES")
                        print(sub_files[n], "has changed content")
                        print("\n --------------------")
                except IndexError:
                    pass
        else:
            print("No change")
            print("There was no changes in the folder")
            print("\n --------------------")

        checker(hashed_list, binary_list, directory, sub_files, sub_dirs)
    if report == 'menu':
        main()
    else:
        checker(hashed_list, binary_list, directory, sub_files, sub_dirs)

def main():
    print("Welcome to Olivers IDS")
    print("What directory do you want to protect?: ")
    directory = str(input(": "))
    if not os.path.isdir(directory):
        print("ERROR: The directory doesn't exist, try again")
        print("\n------------------")
        main()
    sub_dirs = find_subdirs(directory)
    sub_files = find_subfiles(directory)
    print_found(sub_dirs, sub_files)

    binary_list = binary_creator(sub_files)
    hashed_list = hasher(binary_list)
    checker(hashed_list, binary_list, directory, sub_files, sub_dirs)

if __name__ == "__main__":
    main()