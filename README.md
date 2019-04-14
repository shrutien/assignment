# assignment


1. Write a Python program that does the following:

    a. accepts a plaintext file as an argument, so that it may be run as follows:
        python main.py path/to/input_file.txt

    b. prints the number of lines, words and characters in the file.
        (assume UTF-8 encoded file and simple split-on-space tokenization to get words)

    c. writes all unique characters to a file 'out-chars.txt', sorted by frequency (highest to lowest)

    d. writes all unique words to a file 'out-words.txt', sorted by frequency (highest to lowest)

    e. writes all unique 2-grams to a file 'out-bi-grams.txt', sorted by frequency (highest to lowest)
        e.g., for line 'ab cd ef gh', the 2-grams are ['ab cd', 'cd ef', 'ef gh']

    f. writes all unique 3-grams to a file 'out-tri-grams.txt', sorted by frequency (highest to lowest)
        e.g., for line 'ab cd ef gh', the 3-grams are ['ab cd ef', 'cd ef gh']


2. Write a Python program that does the following:

    a. accepts a plaintext file as an argument, so that it may be run as follows:
        python main.py path/to/input_file.txt
        (each line in this file should be a URL)

    b. fetches the URLs in parallel using multiple threads

    c. records and prints the time taken per URL and in total

    d. prints every URL and the first 80 characters of the respective URL's response content

