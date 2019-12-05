from csv_writer_task import create_csv, create_csv_list, create_csv_dictionary
from utils.util import timeit

alphabet, punctuation = [], []

@timeit
def total_words(words):
    """Total no of words"""
    return len(words)

@timeit
def total_alphabet_and_punctuation(words):
    """Total alphabet and punctuations"""
    alphabet_c = punctuation_c = 0
    global alphabet, punctuation
    alphabet, punctuation = [], []
    for word in words:
        for i in range(len(word)):
            if word[i].isalpha():
                alphabet_c += 1
                alphabet.append(word[i])
            elif word[i] in ".?'\",!&:;()[]{}":
                punctuation_c += 1
                punctuation.append(word[i])
    return [len(alphabet), len(punctuation)]

@timeit
def word_frequency(words):
    """Word frequency of all words"""
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

@timeit
def alphabet_and_punctuation_frequencies(text_file):
    """Alphabet frequency and punctuation frequency"""
    count = dict()
    for words in text_file:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1

    return count

@timeit
def alphabetic_word_frequencies(words):
    """Alphabetic word frequencies like a--> 2000"""
    alpha_word = dict()
    for word in words:
        if word[0] in alpha_word:
            alpha_word[word[0]] += 1
        else:
            alpha_word[word[0]] = 1

    return alpha_word

@timeit
def starting_and_ending_with_vowel(words):
    """Starting and ending with vowel"""
    starting_vowel = []
    for word in words:
        if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
            starting_vowel.append(word)

    return starting_vowel

@timeit
def total_sentences(sentences):
    """Total Sentences"""
    return len(sentences)

@timeit
def length_of_sentences(sentences):
    """Longest, shortest and Average length of the sentences"""
    min_l = len(min(sentences, key=len))
    max_l = len(max(sentences, key=len))
    avg = (int(min_l+max_l))/2

    return max_l, min_l, avg


if __name__ == '__main__':
    text = open("2600-0.txt", "r", encoding="utf-8").read().lower()
    text_word = text.split()
    text_sentence = text.replace("\n", "").split("." or "?" or "...")

    create_csv("no_of_words.csv", "Total no Words", total_words(text_word))
    create_csv("no_of_alphabets_and_punctuation.csv", "No of alphabets and punctuations", total_alphabet_and_punctuation(text_word))
    create_csv_dictionary("word_frequencies.csv", "Word frequency", word_frequency(text_word))
    create_csv_dictionary("alphabet_frequencies.csv", "Alphabet frequencies", alphabet_and_punctuation_frequencies(alphabet))
    create_csv_dictionary("punctuation_frequencies.csv", " punctuations frequencies", alphabet_and_punctuation_frequencies(punctuation))
    create_csv_dictionary("alphabetic_word_frequencies.csv", "Alphabetic word frequency", alphabetic_word_frequencies(text_word))
    create_csv_list("starting_and_ending_with_vowel.csv", "All words starting and ending with vowel", starting_and_ending_with_vowel(text_word))
    create_csv("no_of_sentences.csv", "Total sentences", total_sentences(text_sentence))
    create_csv("length_of_sentences.csv", "Longest sentence, shortest sentence and average sentence", length_of_sentences(text_sentence))