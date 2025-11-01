import argparse
from .core import generate_password

def main():
    """
    Defines command-line interface and runs password generation.
    """
    # 1. Configure ArgumentParser.
    parser = argparse.ArgumentParser(
        description="Command line password generator."
    )
    
    # Password length argument.
    parser.add_argument(
        '-l', '--length', 
        type=int, 
        default=12, 
        help="Desired length of the password, by default the value is 12."
    )
    
    # Optional arg to exclude special charaters (flag).
    parser.add_argument(
        '--no-symbols', 
        action='store_true',  # Al estar presente, establece el valor a True
        help="Excludes special characters in the generated password."
    )
    
    # Optional arg to exclude special numbers (flag).
    parser.add_argument(
        '--no-numbers', 
        action='store_true',
        help="Excludes numbers in the generated password."
    )
    
    # 2. Parse the arguments from command line.
    args = parser.parse_args()
    
    # 3. Generate the password.
    # args.no_symbols includes special characters if False
    # args.no_numbers includes numbers if False
    try:
        password = generate_password(
            length=args.length,
            include_symbols=not args.no_symbols,
            include_numbers=not args.no_numbers
        )
        
        # 4. Print the resulting password.
        print(f"\nGenerated password (length: {args.length}):")
        print("-" * (args.length + 30))
        print(f"{password}\n")

    except ValueError as e:
        print(f"\nError: {e}")