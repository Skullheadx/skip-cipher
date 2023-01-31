import wordninja  # pip install wordninja

with open("output/output.txt", "r") as f:  # This is the file you want to split.
    text = f.read()

with open("sentences.txt", "w") as f:  # This is the file you want to write to.
    for line in text.split("\n"):  # Split the text into lines.
        f.write(" ".join(wordninja.split(line)) + "\n")  # Split the lines into words and write them to the file.
