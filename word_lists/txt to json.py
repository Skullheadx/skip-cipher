import json

# Regular version:
# with open("20k.txt", "r") as f:  # word list
#     text = {word: 1 for word in f.read().split("\n")}  # convert the word list to a dictionary
#
# with open("20k.json", "w") as f:  # output file
#     json.dump(text, f, indent=4, sort_keys=False)  # write the dictionary to the output file

# Pruned version:
with open("20k.txt", "r") as f:  # word list
    # convert the word list to a dictionary and remove words with less than 3 characters
    text = {word: 1 for word in f.read().split("\n") if len(word) >= 3}

with open("pruned_20k.json", "w") as f:  # output file
    json.dump(text, f, indent=4, sort_keys=False)  # write the dictionary to the output file
