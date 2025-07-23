from typing import List, Dict
import re

def to_camel_case(name: str) -> str:
    """Convert an underscore_separated string to CamelCase."""
    return ''.join(word.capitalize() for word in name.split('_'))

def insert_and_clobber(main_str: str, insert_str: str, index: int) -> str:
    # Ensure index is within valid range
    if index < 0 or index > len(main_str):
        raise IndexError("Index out of range")
    
    return main_str[:index] + insert_str + main_str[index + len(insert_str):]


def map_words_to_abbreviations(words: List[str]) -> Dict[str, str]:
    """
    Takes a list of unique snake_case words and returns a dictionary mapping
    each word to a unique abbreviation.
    """
    abbreviation_to_word = {}
    word_to_abbreviation = {}

    for word in words:
        abbr = generate_unique_abbreviation(abbreviation_to_word, word)
        word_to_abbreviation[word] = abbr

    return word_to_abbreviation

def generate_abbreviation(snake_case_name: str) -> str:
    """
    Generates an abbreviation from a snake_case name.
    """
    # NOTE: using /, \, _, -, and . as delimiters,
    words = re.split(r'[\/\\_\-\.]', snake_case_name)
    return ''.join(word[0] for word in words if word)


def generate_unique_abbreviation(abbreviation_to_word: Dict[str, str], word_to_abbreviate: str) -> str:
    """
    Ensures a unique abbreviation for a given word based on an abbreviation map.
    
    Args:
        abbreviation_to_word (dict): A dictionary where keys are abbreviations and values are words.
        word_to_abbreviate (str): The word to generate an abbreviation for.
    
    Returns:
        str: A unique abbreviation for the word.
    """
    # Generate the initial abbreviation
    abbreviation = generate_abbreviation(word_to_abbreviate)
    
    # Check for conflicts and resolve them
    if abbreviation in abbreviation_to_word:
        if abbreviation_to_word[abbreviation] != word_to_abbreviate:
            suffix = 1
            original_abbreviation = abbreviation
            while abbreviation in abbreviation_to_word and abbreviation_to_word[abbreviation] != word_to_abbreviate:
                abbreviation = f"{original_abbreviation}{suffix}"
                suffix += 1
    
    # Add the unique abbreviation to the map
    abbreviation_to_word[abbreviation] = word_to_abbreviate
    return abbreviation


