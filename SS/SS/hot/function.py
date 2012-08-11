def rank(words,words_y):
    rank1 = {}
    rank_y = {}
    delta = []
    for word in words:
        i = 1
        rank1[word.value] = i
        i += 1
    for word in words_y:
        i = 1
        rank_y[word.value] = i
        i += 1
    for word in words:
        if not rank_y.__contains__(word.value):
            delta.append(1)
        else:
            if rank1[word.value] < rank_y[word.value]:
                delta.append(1)
            elif rank1[word.value] > rank_y[word.value]:
                delta.append(-1)
            else:
                delta.append(0)
    return delta