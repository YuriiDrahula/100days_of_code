with open(".\\Input\\Letters\\starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    with open(".\\Input\\Names\\invited_names.txt") as invited_names:
        names_list = invited_names.readlines()
        for name in names_list:
            new_name = name.strip('\n')
            new_letter = letter.replace("[name]", new_name)
            new_file = open(f".\\Output\\ReadyToSend\\letter_for_{new_name}.txt", "w")
            new_file.write(new_letter)
            new_file.close()