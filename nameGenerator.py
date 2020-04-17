import random
import json

# Import JSON Files
male_names = json.loads(open('male_names.json').read())
female_names = json.loads(open('female_names.json').read())
surnames = json.loads(open('surnames.json').read())
fantasy_first_names = json.loads(open('fantasy_first_names.json').read())
fantasy_surnames = json.loads(open('fantasy_surnames.json').read())
username_nouns = json.loads(open('username_nouns.json').read())
username_adjectives = json.loads(open('username_adjectives.json').read())

# Variables
name_list = []
whileLoops = True
num_of_names = 0
gender = ''
type_of_name = ''
first_last_name = ''
new_file = ''
overwrite_file = ''
copyandpaste = ''
txtFile = ''

# Introduction to name generator
print('--------------------------------------------------------------\nHello! This is a random name generator, please '
      'answer the following question to get your list of random names!\n'
      '--------------------------------------------------------------')

# Gets number of names between 1 and 50,000
while whileLoops:
    input_v = input("(Disclaimer: When choosing over 5,000 it might take a while!)\n"
                    "How many names do you want?(1 - 50,000):")
    try:
        int(input_v)
        if int(input_v) in range(1, 50001):
            whileLoops = False
            continue
        else:
            print("--------------------------------------------------------------\n"
                  "Please enter a number between 1 and 50,000"
                  "\n--------------------------------------------------------------")
            continue
    except ValueError:
        print("--------------------------------------------------------------\n"
              "Please enter a number between 1 and 50,000"
              "\n--------------------------------------------------------------")
        continue
num_of_names = int(input_v)
whileLoops = True


# Gets  type of name
while whileLoops:
    input_v = input("--------------------------------------------------------------\n"
                    "What type of name do you want?(real, fantasy, or username)")
    try:
        if any(str(input_v).lower() == type_name for type_name in ["real", "fantasy", "username"]):
            whileLoops = False
            continue
    except Exception:
        print("--------------------------------------------------------------\n"
              "Please enter either real, fantasy, or username")
        continue
type_of_name = input_v
whileLoops = True

# Gets first or last name, or both
if any(type_of_name == type_name for type_name in ["real"]):
    if num_of_names < 1001:
        while whileLoops:
            input_v = input("--------------------------------------------------------------\n"
                            "Do you want first or last names, or both?(first, last, both)")
            try:
                if any(str(input_v).lower() == type_name for type_name in ["first", "last", "both"]):
                    whileLoops = False
                    continue
            except Exception:
                print("--------------------------------------------------------------\n"
                      "Please enter either first or last, or both")
                continue
    else:
        input_v = "both"
first_last_name = input_v
whileLoops = True

# Gets gender
if type_of_name == "real":
    while whileLoops:
        if first_last_name != "last":
            input_v = input("--------------------------------------------------------------\n"
                            "What gender?(male, female, or both)")
            try:
                if any(str(input_v).lower() == gender for gender in ["male", "female", "both"]):
                    whileLoops = False
                    continue
            except Exception:
                print("--------------------------------------------------------------\n"
                      "Please enter either male, female, or both")
                continue
        else:
            input_v = "male"
gender = input_v
whileLoops = True

# Put names into a list
for i in range(1, num_of_names + 1):
    whileLoops = True
    while whileLoops:
        if type_of_name == "real":
            if gender == "male":
                if first_last_name == "first":
                    x = random.choice(male_names).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
                elif first_last_name == "last":
                    x = random.choice(surnames).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
                elif first_last_name == "both":
                    x = random.choice(male_names).title() + " " + random.choice(surnames).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
            elif gender == "female":
                if first_last_name == "first":
                    x = random.choice(female_names).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
                elif first_last_name == "last":
                    x = random.choice(surnames).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
                elif first_last_name == "both":
                    x = random.choice(female_names).title() + " " + random.choice(surnames).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
            elif gender == "both":
                if first_last_name == "first":
                    x = random.choice(female_names).title()
                    y = random.choice(male_names).title()
                    z = random.choice([x,y])
                    if z not in name_list:
                        name_list.append(z)
                        whileLoops = False
                        continue
                elif first_last_name == "last":
                    x = random.choice(surnames).title()
                    if x not in name_list:
                        name_list.append(x)
                        whileLoops = False
                        continue
                elif first_last_name == "both":
                    x = random.choice(female_names).title() + " " + random.choice(surnames).title()
                    y = random.choice(male_names).title() + " " + random.choice(surnames).title()
                    z = random.choice([x,y])
                    if z not in name_list:
                        name_list.append(z)
                        whileLoops = False
                        continue
        elif type_of_name == "fantasy":
            x = random.choice(fantasy_first_names).title() + " " + random.choice(fantasy_surnames).title()
            if x not in name_list:
                name_list.append(x)
                whileLoops = False
                continue
        elif type_of_name == "username":
            x = random.choice(username_adjectives) + random.choice(username_nouns).title() + str(random.randint(10, 99))
            if x not in name_list:
                name_list.append(x)
                whileLoops = False
                continue
whileLoops = True
i = 0

# Copy and paste?
while whileLoops:
    copyandpaste = input("--------------------------------------------------------------\n"
                         "Are you going to copy and paste this list?(y/n)")
    try:
        if any(copyandpaste == yesorno for yesorno in ["y","n","yes","no"]):
            whileLoops = False
            continue
    except Exception:
        continue
whileLoops = True

# Print names
print("\n--------------------------------------------------------------\n")
for names in name_list:
    if copyandpaste == "y":
        print(names)
    elif copyandpaste == "n":
        i = i + 1
        print(i, "-", names)
i = 0

# Put list into text file?
while whileLoops:
    txtFile = input("\nDo you want a text file contains all the names?(y/n)")
    if any(txtFile == a for a in ["y", "yes", "n", "no"]):
        whileLoops = False
    else:
        continue

# Put names into text file if selected
overwrite = True
while overwrite:
    new_file = input("What do you want to name the file?")
    try:
        open(f'{new_file}.txt', 'x')
        new_file = open(f'{new_file}.txt', 'w+')
        overwrite = False
        continue
    except Exception:
        whileLoops = True
        while whileLoops:
            overwrite_file = input('This file already exists! Do you want to overwrite it?(y/n)')
            if any(overwrite_file == c for c in ["y", "yes"]):
                new_file = open(f'{new_file}.txt', 'w+')
                whileLoops = False
                overwrite = False
                continue
            elif any(overwrite_file == d for d in ["n", "no"]):
                print("Please think of a different name for your file!")
                continue
            else:
                continue

# Write names to file
if any(txtFile == a for a in ["y", "yes"]):
        if any(copyandpaste == e for e in ["y", "yes"]):
            for names in name_list:
                new_file.write(f'{names}\n')
        elif any(copyandpaste == f for f in ["n", "no"]):
            for names in name_list:
                i = i + 1
                new_file.write(f'{i} - {names}\n')
        new_file.close()

print("Names successfully written to file!")
