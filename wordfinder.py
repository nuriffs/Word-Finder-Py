from trie import Trie
import sys
from typing import List

class WordFinder:
    def __init__(self, board_string, dictionary):
        self.board = []
        self.trie = Trie()
        self.initialize_board(board_string)
        self.initialize_trie(dictionary)

    def initialize_board(self, board_string):
        board_string = board_string.replace("\\n", "\n")
        rows = board_string.split("\n")
        num_rows = len(rows)
        num_cols = len(rows[0])

        self.board = [[''] * num_cols for _ in range(num_rows)]

        for i in range(num_rows):
            for j in range(min(num_cols, len(rows[i]))):
                self.board[i][j] = rows[i][j]

    def initialize_trie(self, dictionary):
        for word in dictionary:
            self.trie.insert(word.lower())

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def search_words(self):
        while True:
            user_input = input("Enter a word to search (or type 'exit' to quit): ").lower()

            if user_input == "exit":
                break

            if self.is_valid_word(user_input):
                if self.trie.search(user_input):
                    print("Word found!")
                else:
                    print("Word not found.")
            else:
                print("Invalid word. Words must be at least three letters in length.")

    def is_valid_word(self, word):
        return len(word) >= 3