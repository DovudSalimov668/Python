import pathlib

# THE OPTIONS:
while True :
    user = input()
    if user == "exit":
        break
    print("Functions of the program:")
    print(" ")
    print("1. List files in a directory (show file name, its size and last modification time)")
    print(" ")
    print("2. Create a new file (user input file name and create it if it does not exists already)")
    print(" ")
    print("3. Create a new directory (show dic's parent's directory, )")
    print(" ")
    print("4. Delete a file (warn a user before deleting)")
    print(" ")
    print("5. Delete a directory (also warm the user)")
    print(" ")
    print("6. Rename a file or directory")
    print(" ")
    print("7. Change a folder (user should be able to change working  directory to another one, and do file operations in new directory)")
    print(" ")

    user_input = int(input("Choose one of options :"))

    if user_input == 1:
        try :
            line_directory = pathlib.Path.cwd()
            for i in line_directory.iterdir():
                print(i, i.stat())
        except:
            print("Your are wrong")
    elif user_input == 2:
        try:
            user_input = input("Enter name your file :")
            line_file = pathlib.Path.cwd()
            new_file = line_file / f"{user_input}"
            if new_file.exists() == True:
                print("You file has in this directory ")
            else :
                new_file.touch()
                print(new_file)
        except:
            print("Your are wrong")

    elif user_input == 3:
        try:
            user_input = input("Enter name your directory :")
            line_directory = pathlib.Path.cwd()
            new_directory = line_directory / f"{user_input}"
            if new_directory.exists() == True:
                print("You directory exist in this place")
            else :
                new_directory.mkdir()
                print(new_directory)
        except:
            print("Your are wrong")
    elif user_input == 4:
        try:
            user_input = input("Enter name your file :")
            line_file = pathlib.Path.cwd()
            new_file = line_file / f"{user_input}"
            if new_file.exists() == True:
                print("You file has in this directory ")
                print("Are sure , that do you want to delite this file")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    new_file.unlink()
                    print(line_file)
                else :
                    pass
        except:
            print("Your are wrong")
    elif user_input == 5:
        try:
            user_input = input("Enter name your directory :")
            line_directory = pathlib.Path.cwd()
            new_directory = line_directory / f"{user_input}"
            if new_directory.exists() == True:
                print("You directory existed in this place")
                print("Are sure , that do you want to delite this directory")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    new_directory.rmdir()
                    print(line_directory)
                else :
                    pass
        except:
            print("Your are wrong")

    elif user_input == 6:
        try:
            user_input = input("Enter name your directory or file, that you used :")
            line_directory_file = pathlib.Path.cwd()
            last_directory = line_directory_file / user_input
            user_input_new_name = input("Enter a new name of your directory or file:")
            new_directory_file = line_directory_file / user_input_new_name

            if last_directory.exists() == True:
                print("You directory or file existed in this place")
                print("Are sure , that do you want to rename this directory or file")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    last_directory.replace(new_directory_file)
                    print(line_directory_file)
                else :
                    pass
        except:
            print("Your are wrong")
    elif user_input == 7 :
        user_input = input("Enter you previose place ")
        old_line = pathlib.Path.cwd()
        print(f"You previos place {old_line}")
        print("Are sure , change your previos place ")
        user_agree = input("YES OR NO\n")
        if user_agree == 'YES':
            user_new_place = input("Enter name of place ")
            new_place = old_line / f"{user_new_place}"
            print(new_place)
        else :
            pass