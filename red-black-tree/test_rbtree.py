import unittest

from rbtree import Tree


class TreeTest(unittest.TestCase):
    def test_insert(self):
        t = Tree()
        t[1] = 'one'
        self.assertEqual(t[1], 'one')
        self.assertEqual(len(t), 1)
        t[2] = 'two'
        self.assertEqual(t[1], 'one')
        self.assertEqual(t[2], 'two')
        self.assertEqual(len(t), 2)


if __name__ == '__main__':
    unittest.main()
