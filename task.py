import csv

text = open("2600-0.txt", "r", encoding="utf-8").read().lower()

words = text.split()

alphabet, punctuation = [], []
alphabet_c = digit_c = punctuation_c = 0
for i in range(len(text)):
    if text[i].isalpha():
        alphabet_c += 1
        alphabet.append(text[i])
    elif text[i].isdigit():
        digit_c += 1
    else:
        new = text[i]
        punctuation_c += 1
        punctuation.append(new)
print("no of alphabets:", len(alphabet))
print("no of punctuation:", len(punctuation))

def counter(x):
    count = dict()
    wordss = x.split()
    for w in wordss:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    return count


tf_word = counter(text)

def counter(x):
    count = dict()
    for w in x:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    return count


tf_alphabet = counter(alphabet)
tf_punctuation = counter(punctuation)

alpha_word = dict()
for word in words:
    if word[0] in alpha_word:
        alpha_word[word[0]] += 1
    else:
        alpha_word[word[0]] = 1

starting_vowel = []
for word in words:
    if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
        starting_vowel.append(word)

sentences = text.replace("\n", "").split("." or "?" or "...")
print(sentences)

print(len(sentences))

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

with open("test.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")

    writer.writerow(["Total_no_Words", len(words)])
    writer.writerow(["No_of_alphabets", len(alphabet)])
    writer.writerow(["No_of_punctuations", len(punctuation)])
    writer.writerow(["Word_freq", counter(text)])
    writer.writerow(["Alphabet_freq", counter(alphabet)])
    writer.writerow(["Punctuation_freq", counter(punctuation)])
    writer.writerow(["Alphabetic word frequency", alpha_word])
    writer.writerow(["All words starting and ending with vowel", starting_vowel])
    writer.writerow(["Total sentences", len(sentences)])
    writer.writerow(["Longest sentence", maxl, "shortest sentence", minl, "Average length of sentence", avg])