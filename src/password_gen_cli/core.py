import random
import string

def generate_password(length: int=12, include_symbols: bool=True, include_numbers: bool=True) -> str:
    """
    Create a random password taking into account the parameters.
    """
    # 1. Define the character set
    characters = string.ascii_letters  # Includes a-zA-Z by default

    if include_numbers:
        characters += string.digits  # Includes 0-9

    if include_symbols:
        # Common symbols for passwords, excluding spaces and quotes
        characters += string.punctuation 

    # 2. Select random characters to form the password
    # random.choice selects a random element from the given sequence
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password