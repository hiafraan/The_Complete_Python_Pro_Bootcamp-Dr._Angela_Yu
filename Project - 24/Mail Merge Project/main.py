# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        new_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, new_name)

        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)