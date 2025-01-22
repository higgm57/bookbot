def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(word_count(file_contents))
    print(character_count(file_contents))
    character_dict = (character_count(file_contents))
    print(report(character_dict))

def word_count(file_contents):
    words = file_contents.split()
    return (len(words))

def character_count(file_contents):
    lowered_string = file_contents.lower()
    character_dict = {}
    for char in lowered_string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def report(character_dict):
    dict_list = []
    for char in character_dict:
        dict_list += char
    def sort_on(char):
        return character_dict[char]
    dict_list.sort(reverse=True, key=sort_on)
    report_statement = []
    for char in dict_list:
        if char.isalpha():
            report_statement.append(f"The '{char}' character was found {character_dict[char]} times")
    return report_statement

main()



