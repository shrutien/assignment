import re
from collections import Counter
from nltk.util import ngrams

unique_word_list = []
lower_case=[]
unique_characters= []
unique_n_grams = []
unique_n_tri_grams=[]

'''Reads Plain text file and reads the number of characters,lines and words in given text file.'''

with open('input_file_1.txt','r') as f:
    lines = 0
    words = 0
    character = 0

    total_words_list = []
    total_characters_list = []
    for line in f.readlines():
        words+=len(line.split())
        character_split= re.sub('[-.,\n]',' ',line)

        lower_case_word = [total_words_list.append(str(lower_string).casefold()) for lower_string in character_split.split()]
        total_characters_list.extend(list(character_split))
        character+=len(list(line))
        lines+=1


    print('Number of lines: ',lines)
    print('number of words: ',words)
    print('NUmber of characters: ',character)


'''Writes unique words to a file sorted by highest frequency'''

words_count = Counter(total_words_list)
unique_words_list = [unique_word_list.append(char) for char, count in words_count.most_common() if
                          char not in unique_word_list]
with open("out-words.txt", "w") as fw:
    fw.writelines("%s\n" % l for l in unique_word_list)


'''Writes unique Characters to a file sorted by highest frequency'''

characters_count = Counter(total_characters_list)
unique_characters_list = [unique_characters.append(char) for char, count in characters_count.most_common() if
                          char not in unique_characters]

with open("out-chars.txt", "w") as fw:
    fw.writelines("%s\n" % l for l in unique_characters)


'''Writes unique 2-grams to a file sorted by highest frequency'''

bi_n_grams = Counter(ngrams(total_words_list, 2))
unique_n_grams_list = [unique_n_grams.append(char) for char, count in bi_n_grams.most_common() if
                          char not in unique_n_grams]

with open("out-bi-grams.txt", "w") as fw:
    fw.writelines("%s\n" % str(l) for l in unique_n_grams)


'''Writes unique 3-grams to a file sorted by highest frequency'''

tri_n_grams = Counter(ngrams(total_words_list, 3))
unique_n_grams_tri_list = [unique_n_tri_grams.append(char) for char, count in tri_n_grams.most_common() if
                          char not in unique_n_tri_grams]

with open("out-tri-grams.txt", "w") as fw:
    fw.writelines("%s\n" % str(l) for l in unique_n_tri_grams)
