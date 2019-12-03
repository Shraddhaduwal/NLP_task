import csv
import time

alphabet, punctuation = [], []

def total_words(words):
    # Total no of words
    return len(words)


def total_alphabet_and_punctuation(words):
    # Total alphabet and punctuations
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
    min_l = len(min(sentences, key=len))
    max_l = len(max(sentences, key=len))
    avg = (int(min_l+max_l))/2

    return max_l, min_l, avg


def create_csv(filename, string, l):
    # Create csv files
    with open("Results/" + filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow([string, l])


def create_csv_dictionary(filename, string, l):
    # Create csv files and arrange the contents in dictionary format
    with open("Results/" + filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow([string])
        for key, value in l.items():
            writer.writerow([key, value])


def timed_call(function_name, arg):
    # Calculates the time taken by the code to be executed
    t0 = time.time()
    result = function_name(arg)
    t1 = time.time()
    print(str(function_name) + " took " + str(t1-t0) + " seconds ")
    return result


def test():
    # Unit testing for every functions
    unit_text = '''This post is for the absolute NLP beginner, but knowledge of Python is assumed. The NLP is famous. We should learn it now.
    '''.lower()

    sample_words_with_punctuations = unit_text.split()
    sample_words_without_punctuations = unit_text.replace(",", '').replace(".", '').split()
    sample_sentences = [sent for sent in unit_text.split("." or "?" or "...") if sent.strip()]
    sample_alphabets = ['t', 'h', 'i', 's', 'p', 'o', 's', 't', 'i', 's', 'f', 'o', 'r', 't', 'h',
                        'e', 'a', 'b', 's', 'o', 'l', 'u', 't', 'e', 'n', 'l', 'p', 'b', 'e', 'g',
                        'i', 'n', 'n', 'e', 'r', 'b', 'u', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd',
                        'g', 'e', 'o', 'f', 'p', 'y', 't', 'h', 'o', 'n', 'i', 's', 'a', 's', 's',
                        'u', 'm', 'e', 'd', 't', 'h', 'e', 'n', 'l', 'p', 'i', 's', 'f', 'a', 'm',
                        'o', 'u', 's', 'w', 'e', 's', 'h', 'o', 'u', 'l', 'd', 'l', 'e', 'a', 'r',
                        'n', 'i', 't', 'n', 'o', 'w']

    sample_punctuations = [',', '.', '.', '.']
    assert total_words(sample_words_without_punctuations) == 23
    assert total_alphabet_and_punctuation(sample_words_with_punctuations) == [96, 4]
    assert word_frequency(sample_words_without_punctuations) == {'this': 1,
                                                                 'post': 1,
                                                                 'is': 3,
                                                                 'for': 1,
                                                                 'the': 2,
                                                                 'absolute': 1,
                                                                 'nlp': 2,
                                                                 'beginner': 1,
                                                                 'but': 1,
                                                                 'knowledge': 1,
                                                                 'of': 1,
                                                                 'python': 1,
                                                                 'assumed': 1,
                                                                 'famous': 1,
                                                                 'we': 1,
                                                                 'should': 1,
                                                                 'learn': 1,
                                                                 'it': 1,
                                                                 'now': 1}
    assert alphabet_and_punctuation_frequencies(sample_alphabets) == {'t': 8,
                                                                      'h': 5,
                                                                      'i': 6,
                                                                      's': 10,
                                                                      'p': 4,
                                                                      'o': 9,
                                                                      'f': 3,
                                                                      'r': 3,
                                                                      'e': 10,
                                                                      'a': 4,
                                                                      'b': 3,
                                                                      'l': 6,
                                                                      'u': 5,
                                                                      'n': 8,
                                                                      'g': 2,
                                                                      'k': 1,
                                                                      'w': 3,
                                                                      'd': 3,
                                                                      'y': 1,
                                                                      'm': 2}
    assert alphabet_and_punctuation_frequencies(sample_punctuations) =={',': 1, '.': 3}
    assert starting_and_ending_with_vowel(sample_words_without_punctuations) == ['absolute']
    assert total_sentences(sample_sentences) == 3
    assert length_of_sentences(sample_sentences) == (78, 18, 48.0)

    return "test pass"


if __name__ == '__main__':
    text = open("2600-0.txt", "r", encoding="utf-8").read().lower()
    text_word = text.split()
    text_sentence = text.replace("\n", "").split("." or "?" or "...")

    a = timed_call(total_words, text_word)
    b = timed_call(total_alphabet_and_punctuation, text_word)
    c = timed_call(word_frequency, text_word)
    d = timed_call(alphabet_and_punctuation_frequencies, alphabet)
    e = timed_call(alphabet_and_punctuation_frequencies, punctuation)
    f = timed_call(alphabetic_word_frequencies, text_word)
    g = timed_call(starting_and_ending_with_vowel, text_word)
    h = timed_call(total_sentences, text_sentence)
    i = timed_call(length_of_sentences, text_sentence)

    create_csv("no_of_words.csv", "Total no Words", a)
    create_csv("no_of_alphabets_and_punctuation.csv", "No of alphabets and punctuations", b)
    create_csv_dictionary("word_frequencies.csv", "Word frequency", c)
    create_csv_dictionary("alphabet_frequencies.csv", "Alphabet frequencies", d)
    create_csv_dictionary("punctuation_frequencies.csv", " punctuations frequencies", e)
    create_csv_dictionary("alphabetic_word_frequencies.csv", "Alphabetic word frequency", f)
    create_csv("starting_and_ending_with_vowel.csv", "All words starting and ending with vowel", g)
    create_csv("no_of_sentences.csv", "Total sentences", h)
    create_csv("length_of_sentences.csv", "Longest sentence, shortest sentence and average sentence", i)

    print(test())
