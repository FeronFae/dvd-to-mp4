import json

settings = {"Working Directory": None ,"Optical Drive": None}

settings["Working Directory"] = input("Please enter the desired output file directory\n>>> ")

drive = input ("Does your device have more than one optical drive? [y/n]\n>>> ")

if drive == "n":
    settings["Optical Drive"] = "/dev/sr0"

if drive == "y":
        settings["Optical Drive"] = input("Please enter the directory of the drive you will be using\n>>> ")

with open("config.json","w") as file:
      json.dump(settings, file, indent = 4)