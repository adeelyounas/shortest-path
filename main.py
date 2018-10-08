from argparse import ArgumentParser

HOLDING_WORD_NONE = 0
HOLDING_WORD_1 = 1
HOLDING_WORD_2 = 2


class WordNotFoundException(Exception):
    pass


class DistanceException(Exception):
    pass


def find_shortest_distance(filename, word1, word2):
    if word1 == word2:
        raise DistanceException('Cannot find distance for the same word!')

    word1 = word1.lower()
    word2 = word2.lower()

    shortest_distance = -1
    holding_word = 0
    index = 0
    index_word_1 = -1
    index_word_2 = -1

    with open(filename, 'r') as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                word = word.lower()
                if word == word1:
                    index_word_1 = index

                    if holding_word == HOLDING_WORD_2:
                        _distance = index_word_1 - index_word_2
                        if shortest_distance < 0 or shortest_distance > _distance:
                            shortest_distance = _distance

                    holding_word = HOLDING_WORD_1

                if word == word2:
                    index_word_2 = index
                    if holding_word == HOLDING_WORD_1:
                        _distance = index_word_2 - index_word_1
                        if shortest_distance < 0 or shortest_distance > _distance:
                            shortest_distance = _distance

                    holding_word = HOLDING_WORD_2

                index += 1

    if shortest_distance < 0:
        raise WordNotFoundException('Both or one of the word was not found in the given file.')

    return shortest_distance - 1


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="Filename with full path", metavar="FILE")

    parser.add_argument("-w1", "--word1", dest="word1",
                        help="Word 1", metavar="WORD1")

    parser.add_argument("-w2", "--word2", dest="word2",
                        help="Word 2", metavar="WORD2")

    args = parser.parse_args()
    distance = find_shortest_distance(filename=args.filename, word1=args.word1, word2=args.word2)

    print('Minimum number of words between "%s" and "%s" are %s' % (args.word1, args.word2, distance))
