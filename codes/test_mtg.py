"""
Tests the mtg file and saves the output in a markdown file.

Revanth Chowdary Ganga, 2023
Patrick Wang, 2023

Resources:
Jelinek 1985 "Markov Source Modeling of Text Generation"
"""

import nltk
from mtg import finish_sentence
import random


def test_generator():
    """Test Markov text generator."""
    corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())

    n_cases = range(1, 11)
    rand_cases = [True, False]
    sent_cases = [
        ["robot"],
        ["she", "was", "not"],
        ["testing", "markov", "text", "generation"],
        ["this", "is", "a", "test", "sentence", "which", "is", "long"],
    ]
    test_case = 1
    with open(
        "/Users/revanth/Documents/MIDS/Semester 1/NLP/assignments/Assignment 1/NLP_Assignment-1_Test-Cases.md",
        "w",
        encoding="utf-8",
    ) as f:
        for x in sent_cases:
            for y in n_cases:
                for z in rand_cases:
                    if z:
                        l = "True (Stochastic)"
                    else:
                        l = "False (Deterministic)"
                        pass

                    f.write(f"Test Case: {test_case:}" + "\n" + "Input:" + "\n")
                    f.write(
                        f"Seed Sentence: {x}, N-Size: {y}, Randomize: {l} "
                        + "\n"
                        + "Output:"
                        + "\n"
                    )
                    words = finish_sentence(x, y, corpus, z)
                    f.write(str(words) + "\n")
                    f.write(
                        "---------------------------------------------------------------------"
                        + "\n"
                    )
                    test_case += 1
                    pass
                pass

            pass
        pass
    pass


if __name__ == "__main__":
    test_generator()
