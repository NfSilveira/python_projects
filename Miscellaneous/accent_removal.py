import unicodedata
import re

# This code shows 4 different ways to remove accentuation in a string's characters.

# This function is a more aggressive way to remove accentuation, and not actually recommended
def remove_non_ascii(string: str) -> str:

    return string.encode('ascii', 'ignore').decode('utf-8').casefold()


# This function returns only characters that show up in the ASCII table
def remove_non_ascii_normalized(string: str) -> str:

    normalized = unicodedata.normalize('NFD', string)

    return normalized.encode('ascii', 'ignore').decode('utf-8').casefold()


# This function normalizes the string by decomposition, and removes the range
# that contains combining characters with a Regular Expression
def remove_combining_regex(string: str) -> str:

    normalized = unicodedata.normalize('NFD', string)

    return re.sub(r'[\u0300-\u036f]', '', normalized).casefold()


# This function uses List Comprehension on each of the string's chars and checking
# if said char is a combining char(has a combining class), removing those combining chars
def remove_combining_fluent(string: str) -> str:

    normalized = unicodedata.normalize('NFD', string)

    return ''.join(
        [l for l in normalized if not unicodedata.combining(l)]
        ).casefold()


if __name__ == '__main__':

    string = 'Atenção \N{SNAKE}'

    # normalized = unicodedata.normalize('NFD', string)
    # print([(l, f'U+{ord(l):04x}', unicodedata.name(l)) for l in normalized])

    print(string)
    print(remove_non_ascii(string))
    print(remove_non_ascii_normalized(string))
    print(remove_combining_regex(string))
    print(remove_combining_fluent(string))

    print(
        remove_combining_regex('Otávio') == remove_combining_fluent('otavio')
    )