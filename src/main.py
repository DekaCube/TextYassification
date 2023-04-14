from nltk.tokenize import word_tokenize
from typing import List

SKIP_WORDS  = {',','.',"n'","'s"}

# trailing i's in stems create matching issues
# for instance Harry gets shortened to Harri
def remove_trailing_i(word_stems : List[str]) -> List[str]:
    return [w if w[-1] != 'i' else w[0:len(w) -1] for w in word_stems]

def match_case(words: List[str], stems: List[str]) -> List[str]:
    matched_words = []
    for index, value in enumerate(words):
        if value[0] != stems[index][0]:
            matched_words.append(value[0] + stems[index][1:])
        else:
            matched_words.append(stems[index])
    
    return matched_words
    
def half_words(words: List[str]) -> List[str]:
    matched_words = []
    for value in words:
        i = int((len(value)/2) + 1)     
        matched_words.append(value[0:i])
    
    return matched_words

# Script Entry
if __name__ == "__main__":

    with open('./input/text.txt', 'r') as file_handle:
        data = file_handle.read()

    words = word_tokenize(data)
    corrected_stems = half_words(words)

    index = 0
    for word in corrected_stems:
        if word in SKIP_WORDS:
            continue
        data = data[0:index] + (data[index:].replace(word, f"**{word}**", 1))
        index = data[index:].find(word) + (len(word)) * 2 + index

    
    with open("./output/text.md", 'w') as file_handle:
        file_handle.write(data)





