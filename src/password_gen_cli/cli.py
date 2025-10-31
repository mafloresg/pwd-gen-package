import argparse
from .core import generate_password

def main():
    """
    Define la interfaz de línea de comandos y ejecuta la generación.
    """
    # 1. Configurar ArgumentParser
    parser = argparse.ArgumentParser(
        description="Command line password generator."
    )
    
    # Argumento requerido para la longitud
    parser.add_argument(
        '-l', '--length', 
        type=int, 
        default=12, 
        help="La longitud deseada para la contraseña (por defecto: 12)."
    )
    
    # Argumento opcional para excluir símbolos (flag)
    parser.add_argument(
        '--no-symbols', 
        action='store_true',  # Al estar presente, establece el valor a True
        help="Excluye los símbolos de la contraseña generada."
    )
    
    # Argumento opcional para excluir números (flag)
    parser.add_argument(
        '--no-numbers', 
        action='store_true',
        help="Excluye los números de la contraseña generada."
    )
    
    # 2. Parsear los argumentos del usuario
    args = parser.parse_args()
    
    # 3. Llamar a la función de generación
    # Usamos not args.no_symbols porque queremos incluir símbolos por defecto
    try:
        password = generate_password(
            length=args.length,
            include_symbols=not args.no_symbols,
            include_numbers=not args.no_numbers
        )
        
        # 4. Imprimir el resultado
        print(f"\nContraseña generada (Longitud: {args.length}):")
        print("-" * (args.length + 30))
        print(f"{password}\n")

    except ValueError as e:
        print(f"\nError: {e}")