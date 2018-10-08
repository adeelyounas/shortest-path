import os
import unittest
from main import find_shortest_distance, WordNotFoundException, DistanceException


class MainTestCase(unittest.TestCase):
    TEST_TEXT_FILE = './test_text_file'

    SUCCESS_TEST_DATA = [
        {
            'text': 'We do value and reward motivation in our development team. Development is a key skill for a DevOp',
            'word_1': 'motivation',
            'word_2': 'development',
            'result': 2
        },
        {
            'text': 'We do value and reward motivation development team. Development is a key skill for a DevOp',
            'word_1': 'development',
            'word_2': 'motivation',
            'result': 0
        },
        {
            'text': 'We do value and reward motivation development team. Development is a key skill for a DevOp',
            'word_1': 'motivation',
            'word_2': 'Development',
            'result': 0
        }
    ]

    EXCEPTION_TEST_DATA = [
        {
            'text': 'We do value and reward in our development team. Development is a key skill for a DevOp',
            'word_1': 'motivation',
            'word_2': 'development',
            'raises': WordNotFoundException
        },
        {
            'text': 'We do value and reward motivation development team. Development is a key skill for a DevOp',
            'word_1': 'motivation',
            'word_2': 'motivation',
            'raises': DistanceException
        }
    ]

    def setUp(self):
        open(self.TEST_TEXT_FILE, 'a').close()

    def tearDown(self):
        os.remove(self.TEST_TEXT_FILE)

    def _update_file_text(self, text):
        with open(self.TEST_TEXT_FILE, 'w') as f:
            f.write(text)

    def test_distances(self):
        for data in self.SUCCESS_TEST_DATA:
            self._update_file_text(data['text'])
            self.assertEqual(
                find_shortest_distance(filename=self.TEST_TEXT_FILE, word1=data['word_1'], word2=data['word_2']),
                data['result']
            )

    def test_distances_raises_exception(self):
        for data in self.EXCEPTION_TEST_DATA:
            self._update_file_text(data['text'])
            self.assertRaises(
                data['raises'],
                find_shortest_distance,
                filename=self.TEST_TEXT_FILE,
                word1=data['word_1'],
                word2=data['word_2']
            )


if __name__ == "__main__":
    unittest.main()
