from colorama import Style, Fore


YELLOW = Style.BRIGHT + Fore.YELLOW # Color yellow for general important info
RED    = Style.BRIGHT + Fore.RED    # Color red for something bad or info related to the bad guy
CYAN   = Style.BRIGHT + Fore.CYAN   # Color cyan for something good
END_COLOR  = Style.RESET_ALL
CLEAR_SCREEN = "\033[2J"


SPEAK = "You:        "


def decor():
    print("-" * 79)


def print_decor(*args):
    print(*args)
    decor()


def print_input(*args):
    print(*args)
    input()
