from trie import Trie, TrieNode
from wordfinder import WordFinder
from utils import read_word_list_from_file

def main():
    try:
        with open("wordBoard.txt") as board_file:
            board_string = board_file.read()

        dictionary = read_word_list_from_file("wordList.txt")

        word_search = WordFinder(board_string, dictionary)
        word_search.print_board()
        word_search.search_words()

    except IOError as e:
        print(f"Error reading the board file: {e}")

if __name__ == "__main__":
    main()