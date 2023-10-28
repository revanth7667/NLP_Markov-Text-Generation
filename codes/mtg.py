""" 
IDS-703 Fall-23
Assignment 1: Markov Text Generator
Name : Revanth Chowdary Ganga

"""
import random


def finish_sentence(sentence, n, corpus, randomize=False):
    answer = sentence.copy()  # performing deep copy for future purposes
    main_dict = create_dict(
        corpus, n
    )  # This is the primary dcitionary that will be used

    # add word one by one
    continue_flag = True  # used to terminate adding words to answer

    while continue_flag:
        next_word = find_next_word(main_dict, n, answer, randomize, corpus)
        answer.append(next_word)
        if (next_word in [".", "?", "!"]) or (len(answer) == 10):
            continue_flag = False
            pass
        pass

    return answer


def create_dict(corp, n):
    """Uses the tokenized corpus to create a dict with keys of length n and their counts as values"""
    ans_dict = dict()
    for i in range(len(corp) - (n - 1)):
        temp_key = tuple(corp[i : i + n])
        ans_dict[temp_key] = ans_dict.get(temp_key, 0) + 1
    return ans_dict


def max_count(temp_dicti, randomize):
    """returns the word with the max probability in case randomize=Fasle,
    else return any possible word if randomize=True"""

    if randomize:
        # All the Keys have the same initial words so for last word we can pick a random key and extract last item
        return random.choice(list(temp_dicti.keys()))[-1]

    # if random is false, return the last item from the key with the highest value
    return max(temp_dicti, key=lambda x: temp_dicti[x])[-1]


def find_next_word(dicti, n, answer, randomize, corp):
    """Returns the next word to be added to the answer"""
    shorlist_dict = (
        dict()
    )  # to store the key-value pairs which start with the required words

    # Special condition if unigram
    if n == 1:
        new_dict = create_dict(corp, 1)
        return max_count(new_dict, randomize)

    # if not unigram try to find match or perform backoff till found

    # get all keys which have the value:
    for i in dicti.keys():
        if list(i[: n - 1]) == answer[-n + 1 :]:
            shorlist_dict[i] = dicti[i]
            pass
        pass

    if (len(shorlist_dict) == 0) or (len(answer) < n - 1):
        # do stupid backoff
        # create new dict with reduced n:
        new_dict = create_dict(corp, n - 1)

        # do recursive call to find_next_word
        return find_next_word(new_dict, n - 1, answer, randomize, corp)

    # Else return the word with max probability
    return max_count(shorlist_dict, randomize)


if __name__ == "__main__":
    corp = ["testing", "1", "2", "3", "testing", "1", "2", "4", "1", "2", "4"]

    print(
        finish_sentence(
            [
                "testing",
                "1",
            ],
            3,
            corp,
        )
    )
    pass
