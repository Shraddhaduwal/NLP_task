from task import total_words, total_alphabet_and_punctuation, word_frequency, alphabet_and_punctuation_frequencies,\
    alphabetic_word_frequencies, starting_and_ending_with_vowel, total_sentences, length_of_sentences

def test():
    """Unit testing for every functions"""
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
    assert alphabetic_word_frequencies(sample_words_without_punctuations) == {'t': 3,
                                                                              'p': 2,
                                                                              'i': 4,
                                                                              'f': 2,
                                                                              'a': 2,
                                                                              'n': 3,
                                                                              'b': 2,
                                                                              'k': 1,
                                                                              'o': 1,
                                                                              'w': 1,
                                                                              's': 1,
                                                                              'l': 1}
    assert starting_and_ending_with_vowel(sample_words_without_punctuations) == ['absolute']
    assert total_sentences(sample_sentences) == 3
    assert length_of_sentences(sample_sentences) == (78, 18, 48.0)

    return "test pass"


if __name__ == '__main__':
    print(test())
