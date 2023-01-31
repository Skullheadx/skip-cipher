import string  # For punctuation
from math import gcd  # Greatest common divisor


def main():  # Main function
    with open("input/input.txt", "r") as f:  # Open the file
        text = clean_text(f.read())  # Read the file and clean it

    outputs = []  # List of output
    for skip in find_coprimes(len(text)):  # Find all coprimes of the length of the text
        outputs.append(decode(text, skip))  # Decode the text and append it to the output list with different skips

    with open("output/output.txt", "w") as f:  # Open the output file
        f.write("\n".join(outputs))  # Write the output to the file


def clean_text(text):  # Clean the text
    exclude = set(string.punctuation)  # Exclude punctuation
    exclude.add("\n")  # Exclude newlines
    exclude.add(" ")  # Exclude spaces
    text = ''.join(ch for ch in text if ch not in exclude)  # Remove all the excluded characters
    return text  # Return the cleaned text


def decode(text, skip):  # Decode the text
    output = ""  # Output string
    for i in range(len(text)):  # Loop through the text
        output += text[i * skip % len(text)]  # Add the character to the output string
    return output  # Return the output string


def find_coprimes(n):  # Find all coprimes of n
    coprimes = []  # List of coprimes
    for i in range(2, n):  # 2 is the smallest coprime needed for our purposes.
        if gcd(i, n) == 1:  # If the gcd is 1, then the numbers are coprime
            coprimes.append(i)  # Append the coprime to the list
    return coprimes  # Return the list of coprimes


if __name__ == "__main__":  # If the file is run directly
    main()  # Run the main function
