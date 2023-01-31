# Skip cipher

## What is the Skip cipher?

The skip cipher, also known as the jump cipher,
which reorders the letters in a message by skipping a certain number of letters until all the letters have been processed.
In the code, I have set it to add in every possible initial character to begin the skip cipher.

## Dependencies
- Python 3.6 or higher
- wordninja (pip install wordninja)

## How to use the Skip cipher?
1. Enter the encrypted message into input.txt file (or use the default message)
2. Run the main.py file
3. All possible decrypted messages will be saved in output.txt file
4. Run to_sentences.py to turn the decrypted messages into sentences
5. All possible decrypted sentences will be saved in sentences.txt file
6. Run filter_sentences.py to filter the sentences and save the most likely sentences in filtered_sentences.txt file
7. Enjoy the newly decrypted messages!

## Warning:
My code is not perfect and terribly inefficient, so it might take a while to decrypt longer messages.


## References
- https://www.dcode.fr/skip-cipher
- https://github.com/first20hours/google-10000-english
