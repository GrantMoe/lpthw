def scan(input):
    words = input.split()
    results = []
    for word in words:
        token = 'error'
        try:
            word = int(word)
            token = 'number'
        except:
            for word_type in lexicon:
                if word.lower() in lexicon[word_type]:
                    token = word_type
                    break
        results.append((token, word))
    return results


lexicon = {
    'direction': ['north', 'south', 'east', 'west',
                  'down', 'up', 'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet'],
}

#words = input()
#print(words.split())
#split_words = words.split()
#print(scan(words))
#for word in split_words:
#    print(word)