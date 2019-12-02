import csv

alphabet, punctuation = [], []

def total_words(words):
    # Total no of words
    return len(words)


def total_alphabet_and_punctuation(words):
    # Total alphabet and punctuations
    alphabet_c = punctuation_c = 0
    for word in words:
        for i in range(len(word)):
            if word[i].isalpha():
                alphabet_c += 1
                alphabet.append(word[i])
            elif word[i] in ".?'\",!&:;()[]{}":
                punctuation_c += 1
                punctuation.append(word[i])

    return len(alphabet), len(punctuation)


def word_frequency(words):
    # Word frequency of all words:
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


def alphabet_and_punctuation_frequencies(text_file):
    # Alphabet frequency and punctuation frequency
    count = dict()
    for words in text_file:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1

    return count


def alphabetic_word_frequencies(words):
    # Alphabetic word frequencies like a--> 2000
    alpha_word = dict()
    for word in words:
        if word[0] in alpha_word:
            alpha_word[word[0]] += 1
        else:
            alpha_word[word[0]] = 1

    return alpha_word


def starting_and_ending_with_vowel(words):
    # Starting and ending with vowel
    starting_vowel = []
    for word in words:
        if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
            starting_vowel.append(word)

    return starting_vowel


def total_sentences(sentences):
    # Total Sentences
    return len(sentences)


def length_of_sentences(sentences):
    # Longest, shortest and Average length of the sentences
    maxl = 0
    minl = 1
    list = []
    for sentence in sentences:
        length = len(sentence)
        list.append(length)
        if length > maxl:
            maxl = length
        elif length < minl:
            minl = length
    avg = (minl+maxl)/2

    return maxl, minl, avg


def create_csv(filename, string, l):
    # Create csv files
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow([string, l])


def create_csv_dictionary(filename, string, l):
    # Create csv files and arrange the contents in dictionary format
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow([string])
        for key, value in l.items():
            writer.writerow([key, value])


if __name__ == '__main__':
    text = open("2600-0.txt", "r", encoding="utf-8").read().lower()
    text_word = text.split()
    text_sentence = text.replace("\n", "").split("." or "?" or "...")

    create_csv("no_of_words.csv", "Total no Words", total_words(text_word))
    create_csv("no_of_alphabets_and_punctuation.csv", "No of alphabets and punctuations", total_alphabet_and_punctuation(text_word))
    create_csv_dictionary("word_frequencies.csv", "Word frequency", word_frequency(text_word))
    create_csv_dictionary("alphabet_frequencies.csv", "Alphabet frequencies", alphabet_and_punctuation_frequencies(alphabet))
    create_csv_dictionary("punctuation_frequencies.csv", " punctuations frequencies", alphabet_and_punctuation_frequencies(punctuation))
    create_csv_dictionary("alphabetic_word_frequencies.csv", "Alphabetic word frequency", alphabetic_word_frequencies(alphabet))
    create_csv("starting_and_ending_with_vowel.csv", "All words starting and ending with vowel", starting_and_ending_with_vowel(text_word))
    create_csv("no_of_sentences.csv", "Total sentences", total_sentences(text_sentence))
    create_csv("length_of_sentences.csv", "Longest sentence, shortest sentence and average sentence", length_of_sentences(text_sentence))