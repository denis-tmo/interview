import unittest
from word     import test_word_frequency
from password import test_valid_password
from circular import CircularQueue

class TestMethods(unittest.TestCase):

    def test_word(self):
        dict = test_word_frequency('this is a unit test to test')
        val = dict['test']
        self.assertEqual(val, 2)

    def test_password(self):
        pwd = 'asweY76*#'
        valid = test_valid_password(pwd)
        self.assertTrue(valid)

    def test_circular(self):
        max_size = 3
        cqueue = CircularQueue(maxlen=max_size)
        # Add items
        for i in range(1, max_size + 1):
            cqueue.enqueue( 'key' + str(i) , 'value' + str(i))

        # Add more items, only last item will be inserted
        for i in range(max_size + 1, max_size + 3):
            cqueue.enqueue( 'key' + str(i) , 'value' + str(i))

        self.assertEqual(cqueue.get('key5'), 'value5')
        last_item = cqueue.popitem(last=True)
        self.assertEqual(last_item, ('key5', 'value5'))

if __name__ == '__main__':
    unittest.main()
    