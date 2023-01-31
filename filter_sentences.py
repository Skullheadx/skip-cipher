import json

with open("sentences.txt", "r") as f:  # This is the output from to_sentence.py
    text = f.read()  #

with open("word_lists/pruned_20k.json", 'r') as f:  # word list
    word_list = json.load(f)


def filter_text(line):  # filter the text to only include words in the word list and sentences with at least 2 words
    min_sentence_length = 2  # minimum sentence length

    output = []  # output list
    buffer = []  # buffer list (buffer is a temporary list)
    for word in line.split():  # split the line into words
        if word in word_list:  # if the word is in the word list
            buffer.append(word)  # add the word to the buffer list
        else:  # if the word is not in the word list
            if len(buffer) >= min_sentence_length:  # if the buffer list has at least 2 words
                output.append(" ".join(buffer))  # add the buffer list to the output list
            buffer = []  # clear the buffer list
    if len(buffer) >= min_sentence_length:  # if the buffer list has at least 2 words
        output.append(" ".join(buffer))  # add the buffer list to the output list
    return output  # return the output list


with open("output/filter_sentences.txt", "w") as f:  # output file
    for line in text.split("\n"):  # split the text into lines
        # write the filtered lines to the output file with a separator between sentences
        f.write(" | ".join(filter_text(line)) + "\n")
