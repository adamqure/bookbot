def get_words_in_book(text: str):
    return len(text.split())


def get_unique_characters_in_book(text: str):
    dict = {}
    for character in text.lower():
        if character in dict:
            instances = dict[character]
            dict[character] = instances + 1
        else:
            dict[character] = 1
			
    return dict


def sort_on(dict):
    return dict["num"]

def generate_sorted_character_list(character_dict):
    output = []

    for key in character_dict:
        if key.isalpha():
            output.append({
                "char": key,
                "num": character_dict[key]
            })

    output.sort(reverse=True, key=sort_on)
    return output