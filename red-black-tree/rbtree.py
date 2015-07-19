class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def find(cls, node, key):
        if node is None:
            raise KeyError(key)
        elif key == node.key:
            return node.value
        elif key < node.key:
            return cls.find(node.left, key)
        else:
            return cls.find(node.right, key)

    @classmethod
    def insert(cls, node, key, value):
        if node is None:
            node = Node(key, value)
            inserted = True
        elif key == node.key:
            node.value = value
            inserted = False
        elif key < node.key:
            inserted, node.left = cls.insert(node.left, key, value)
        else:
            inserted, node.right = cls.insert(node.right, key, value)
        return inserted, node


class Tree:
    def __init__(self):
        self._root = None
        self._length = 0

    def __setitem__(self, key, value):
        inserted, self._root = Node.insert(self._root, key, value)
        if inserted:
            self._length += 1

    def __getitem__(self, key):
        return Node.find(self._root, key)

    def __len__(self):
        return self._length
