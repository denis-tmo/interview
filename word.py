from collections import OrderedDict

# test word frequency in line
def test_word_frequency(line):
    dict = {}
    line = line.split()
    for word in line:
        data = dict.get(word)
        if data is None:
            dict.update({word : 1})
        else:
            data += 1
            dict.update({word: data})

    dict = OrderedDict(sorted(dict.items()))
    for key, data in dict.items():
        print(f'{(key, data)}')