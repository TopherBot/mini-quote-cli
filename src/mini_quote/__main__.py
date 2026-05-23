import random
from .quotes import QUOTES

def main() -> None:
    """Print a random quote to stdout."""
    print(random.choice(QUOTES))

if __name__ == '__main__':
    main()
