def createFile():
    overwrite = True
    while overwrite:
        new_file_name = input("What do you want to call your file?")
        try:
            open(f'{new_file_name}.txt', 'x')
            new_file = open(f'{new_file_name}.txt', 'x')
            overwrite = False
            new_file.close()
            continue
        except Exception:
            whileLoops = True
            while whileLoops:
                overwrite_file = input('This file already exists! Do you want to overwrite it?(y/n)')
                if any(overwrite_file == c for c in ["y", "yes"]):
                    new_file = open(f'{new_file_name}.txt', 'w')
                    whileLoops = True
                    overwrite = False
                    new_file.close()
                    continue
                elif any(overwrite_file == d for d in ["n", "no"]):
                    whileLoops = False
                    print("Please think of a different name for your file!")
                    continue
                else:
                    continue