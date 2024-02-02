def read_word_list_from_file(file_path):
    with open(file_path) as file:
        return [line.strip().lower() for line in file]