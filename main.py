from typing import List, Dict


def insert_and_clobber(main_str: str, insert_str: str, index: int) -> str:
    # Ensure index is within valid range
    if index < 0 or index > len(main_str):
        raise IndexError("Index out of range")
    
    return main_str[:index] + insert_str + main_str[index + len(insert_str):]


def generate_abbreviation(snake_case_name: str) -> str:
    """
    Generates an abbreviation from a snake_case name.
    """
    words = snake_case_name.split('_')
    return ''.join(word[0].upper() for word in words if word)


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


