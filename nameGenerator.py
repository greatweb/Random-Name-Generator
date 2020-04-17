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

# Introduction to name generator
print('--------------------------------------------------------------\nHello! This is a random name generator, please answer the following question to get your list of random names!\n--------------------------------------------------------------')

# Gets number of names between 1 and 50,000
while whileLoops == True:
    input_v = input("(Disclaimer: When choosing over 5,000 it might take a while!)\nHow many names do you want?(1 - 50,000):")
    try:
        int(input_v)
        if int(input_v) in range(1, 50001):
            whileLoops = False
            continue
        else:
            print("--------------------------------------------------------------\nPlease enter a number between 1 and 50,000")
            continue
    except ValueError:
        print("--------------------------------------------------------------\nPlease enter a number between 1 and 50,000")
        continue
num_of_names = int(input_v)
whileLoops = True


# Gets  type of name
while whileLoops == True:
    input_v = input("--------------------------------------------------------------\nWhat type of name do you want?(real, fantasy, or username)")
    try:
        if any(str(input_v).lower() == type_name for type_name in ["real", "fantasy", "username"]):
            whileLoops = False
            continue
    except Exception:
        print("--------------------------------------------------------------\nPlease enter either real, fantasy, or username")
        continue
type_of_name = input_v
whileLoops = True


# Gets gender
if type_of_name == "real":
    while whileLoops == True:
        input_v = input("--------------------------------------------------------------\nWhat gender?(male, female, or both)")
        try:
            if any(str(input_v).lower() == gender for gender in ["male", "female", "both"]):
                whileLoops = False
                continue
        except Exception:
            print("--------------------------------------------------------------\nPlease enter either male, female, or both")
            continue
gender = input_v
whileLoops = True


# Gets first or last name, or both
if any(type_of_name == type_name for type_name in ["real"]):
    if num_of_names < 1001:
        while whileLoops == True:
            input_v = input("--------------------------------------------------------------\nDo you want first or last names, or both?(first, last, both)")
            try:
                if any(str(input_v).lower() == type_name for type_name in ["first", "last", "both"]):
                    whileLoops = False
                    continue
            except Exception:
                print("--------------------------------------------------------------\nPlease enter either first or last, or both")
                continue
    else:
        input_v = "both"
first_last_name = input_v
whileLoops = True

# Put names into a list
for i in range(1, num_of_names + 1):
    whileLoops = True
    while whileLoops == True:
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
while whileLoops == True:
    copyandpaste = input("--------------------------------------------------------------\nAre you going to copy and paste this list?(y/n)")
    try:
        if any(copyandpaste == yesorno for yesorno in ["y","n","yes","no"]):
            whileLoops = False
            continue
    except Exception:
        continue

# Print names
print("\n--------------------------------------------------------------\n")
for names in name_list:
    if copyandpaste == "y":
        print(names)
    elif copyandpaste == "n":
        i = i + 1
        print(i, "-", names)

