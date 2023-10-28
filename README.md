# Markov Text Generation

[![CI](https://github.com/revanth7667/NLP_Markov-Text-Generation/actions/workflows/cicd.yml/badge.svg)](https://github.com/revanth7667/NLP_Markov-Text-Generation/actions/workflows/cicd.yml)

Implementing a simple Markov Text Generator using N-Grams and Stupid Backoff.

This project was done as part of the Natural Language Processing course at Duke University by [Patrick Wang](https://scholar.google.com/citations?user=KJ3GMlMAAAAJ&hl=en)

Implementing a function of the form:

```console
finish_sentence(sentence, n, corpus, randomize=False)
```

that takes four arguments: 
- sentence: [list of strings] tokens which will be the seed for the sentence to build
- n: [int] the length of n-grams to use for prediction
- corpus: [list of strings] source tokens which will be used as the corpus to predict the next word
- randomize:[Bool] flag to indicating whether the process should be random (stochastic) or deterministic

and returns an extended sentence until the first ., ?, or ! is found OR until it has 10 total tokens.

If the input flag randomize is false:
the code chooses at each step the single most probable next token. if two tokens are equally probable, choose the one that occurs first in the corpus. 

If the input flag randomize is True:
The code draws the next word randomly from the possible tokens.

In-case a valid token is not found for the given n-gram, the code performs **Stupid Backoff** with N-1 recursively till a match is found.
In case No-Match is found evan at N=2, The code returns adds the token with the maximum occurence in the corpus if Random is set False or a random token from the corpus if random flag is set as True 

Sample Input: 'She was not', with N=3 and Random=False
Sample Output: 'She was not in the world.'

