import sys
from stats import get_words_in_book, get_unique_characters_in_book, generate_sorted_character_list

def get_book_text(filepath: str) -> str:
	with open(filepath) as file:
		contents = file.read()
		return contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	print("============ BOOKBOT ============")
	file_path = sys.argv[1]
	print(f"Analyzing book found at {file_path}")
	book_text = get_book_text(file_path)

	print("----------- Word Count ----------")
	print(f"Found {get_words_in_book(book_text)} total words")
	print("--------- Character Count -------")
	character_dict = generate_sorted_character_list(get_unique_characters_in_book(book_text))
	for character in character_dict:
		print(f"{character["char"]}: {character["num"]}")
	print("============= END ===============")


main()
