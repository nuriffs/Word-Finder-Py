from trienode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isEndOfWord = True

    def search(self, word):
        node = self.search_prefix(word)
        return node is not None and node.isEndOfWord

    def starts_with(self, prefix):
        return self.search_prefix(prefix) is not None

    def search_prefix(self, prefix):
        current = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if current.children[index] is None:
                return None
            current = current.children[index]
        return current
