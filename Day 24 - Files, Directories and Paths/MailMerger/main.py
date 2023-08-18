with open("./Input/Names/invited_names.txt") as names_file:
    all_names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as template:
    content = template.read()
    for name in all_names:
        stripped_name = name.strip()
        new_letter = content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)