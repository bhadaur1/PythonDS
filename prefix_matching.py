"""
Given a vocabulary list and a query, find all words that are in the vocabulary

vocabulary = ["kit", "king", "cat", "dog", "can", "kangaroo", "kin"]
query = "ki"

returns = ['kit', 'kin', 'king']
"""

from typing import List


class TrieNode(object):
    def __init__(self, val=None, isword=False) -> None:
        self.val = val
        self.children = set()
        self.isword = isword

    def __repr__(self) -> str:
        return f"""TrieNode: (value={self.val}, isword = {self.isword}, 
                 children = {self.children})\n\n"""


class Trie(object):
    def __init__(self):
        self.head = TrieNode()

    def add_word_to_vocabulary(self, word) -> None:

        """
        Add a word to the trie by moving char by char
        """

        def addchar(char, curr) -> TrieNode:
            """
            Inner function
            Adds a char to the trie
            If node with char value exists, return that node
            else create a new node with char value and return new node
            """
            for child in curr.children:
                if child.val == char:
                    return child
            # print(f"Creating newnode with {char}")
            newnode = TrieNode(char)
            curr.children.add(newnode)
            return newnode

        # Adding word here
        curr = self.head
        for char in word:
            curr = addchar(char, curr)
        curr.isword = True

    def get_word_beginning_with(self, query) -> List:

        words = []  # The answer
        slate = list(query)  # temp cache to append chars to
        curr = self.head

        def movebychar(char, curr) -> TrieNode:
            for child in curr.children:
                if child.val == char:
                    return child
            return None  # Couldn't find child, return None

        def add_word_with_dfs(curr) -> None:
            if curr is None:
                return
            if curr.isword:
                # print("".join(slate))
                words.append("".join(slate[:]))
            for child in curr.children:
                if child is not None:
                    slate.append(child.val)
                    add_word_with_dfs(child)
                    slate.pop()  # remember to pop the slate to be consistent with recursion stack pops

        # Find subtree that begins with last query character
        for char in query:
            curr = movebychar(char, curr)
            if curr is None:  # Cant go any further
                break

        # At this point, we have found a subtree
        # with its root node value equal to last of query char
        # Recursively traverse and append to words
        add_word_with_dfs(curr)

        return words


if __name__ == "__main__":
    trie = Trie()
    vocabulary = ["kit", "king", "cat", "dog", "can", "kangaroo", "kin"]
    query = "ki"

    # Insert into trie
    for word in vocabulary:
        trie.add_word_to_vocabulary(word)

    # all words beginning with "ki"
    print(trie.get_word_beginning_with("ki"))
    # >>> ['kit', 'kin', 'king']

    # all words beginning with "ca"
    print(trie.get_word_beginning_with("ca"))
    # >>> ['cat', 'can']
