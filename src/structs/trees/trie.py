class TrieNode:
    """
    A node in the trie structure.

    Attributes:
    children (dict): A dictionary mapping characters to TrieNode.
    end_of_word (bool): Flag indicating if a node is the end of a word.
    """

    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    """
    Trie data structure class.

    Methods:
    insert(word): Inserts a word into the trie.
    search(word): Returns True if the word is in the trie.
    startsWith(prefix): Returns True if there is any word in the trie that starts with the given prefix.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.

        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> "apple" in trie.root.children
        True
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.

        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.search("apple")
        True
        >>> trie.search("app")
        False
        """
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.end_of_word

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.

        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.starts_with("app")
        True
        >>> trie.starts_with("apl")
        False
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def __contains__(self, word):
        """
        Checks if a word is in the trie using the 'in' operator.

        >>> trie = Trie()
        >>> trie.insert("hello")
        >>> "hello" in trie
        True
        >>> "world" in trie
        False
        """
        return self.search(word)

    def __repr__(self):
        """
        Returns a string representation of the Trie with all its words.

        >>> trie = Trie()
        >>> trie.insert("cat")
        >>> trie.insert("car")
        >>> repr(trie)
        'Trie(['cat', 'car'])'
        """
        words = []
        self._collect_words(self.root, "", words)
        return "Trie(" + ", ".join(words) + ")"

    def _collect_words(self, node, prefix, words):
        if node.end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            self._collect_words(next_node, prefix + char, words)

    def __iter__(self):
        """
        Initializes the iterator for the Trie. Prepares a stack for DFS traversal.

        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.insert("app")
        >>> iterator = iter(trie)
        >>> next(iterator)
        'app'
        """
        self._stack = [(self.root, "")]
        return self

    def __next__(self):
        """
        Returns the next word in the Trie in a DFS manner.

        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.insert("app")
        >>> iterator = iter(trie)
        >>> next(iterator)
        'app'
        >>> next(iterator)
        'apple'
        >>> next(iterator)
        Traceback (most recent call last):
            ...
        StopIteration
        """
        while self._stack:
            node, prefix = self._stack.pop()
            if node.end_of_word:
                return prefix
            for char, next_node in sorted(node.children.items(), reverse=True):
                self._stack.append((next_node, prefix + char))
        raise StopIteration
