"""ASCII art utilities for kudosx."""

import random
import shutil

from kudosx import __version__, __package_name__

RESET = "\033[0m"
PRIMARY_COLOR = "\033[38;2;215;119;87m"  # d77757
LIGHT_COLOR = "\033[38;2;235;159;127m"   # #eb9f7f (light d77757)
WHITE_COLOR = "\033[38;2;255;255;255m"
GRAY_COLOR = "\033[38;2;99;99;99m"
BG_COLOR = "\033[48;2;30;30;30m"  # dark background
ITALIC = "\033[3m"

QUOTES = [
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("The best error message is the one that never shows up.", "Thomas Fuchs"),
    ("It's not a bug; it's an undocumented feature.", "Anonymous"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Build something people want.", "Y Combinator"),
    ("If you're not embarrassed by v1, you launched too late.", "Reid Hoffman"),
    ("Done is better than perfect.", "Sheryl Sandberg"),
    ("Fall in love with the problem, not the solution.", "Uri Levine"),
    ("Step 1: Make the requirements less dumb.", "Elon Musk"),
    ("Step 2: Delete the part or process.", "Elon Musk"),
    ("Step 3: Simplify or optimize.", "Elon Musk"),
    ("Step 4: Accelerate cycle time.", "Elon Musk"),
    ("Step 5: Automate.", "Elon Musk"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("Clean code reads like well-written prose.", "Grady Booch"),
    ("Any fool can write code that a computer can understand.", "Martin Fowler"),
    ("Leave the code cleaner than you found it.", "Robert C. Martin"),
    ("Programs must be written for people to read.", "Harold Abelson"),
    ("Good code is its own best documentation.", "Steve McConnell"),
    ("Refactoring is paying off technical debt.", "Ward Cunningham"),
    ("The ratio of time spent reading vs writing code is 10:1.", "Robert C. Martin"),
    ("A function should do one thing and do it well.", "Unix Philosophy"),
    ("Naming is the hardest problem in computer science.", "Phil Karlton"),
    ("Deleted code is debugged code.", "Jeff Sickel"),
]

BASE_ART = [
    "                                                        ",
    "  ██╗  ██╗██╗   ██╗██████╗  ██████╗ ███████╗██╗   ██╗  ",
    "  ██║ ██╔╝██║   ██║██╔══██╗██╔═══██╗██╔════╝╚██╗ ██╔╝  ",
    "  █████╔╝ ██║   ██║██║  ██║██║   ██║███████╗ ╚████╔╝   ",
    "  ██╔═██╗ ██║   ██║██║  ██║██║   ██║╚════██║ ██╔═██╗   ",
    "  ██║  ██╗╚██████╔╝██████╔╝╚██████╔╝███████║██╔╝  ██╗  ",
    "  ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝  ",
    "                                                        ",
]


def colorize(text: str) -> str:
    """Apply colors to ASCII art characters."""
    colored = ""
    for char in text:
        if char == "█":
            colored += PRIMARY_COLOR + char + RESET
        elif char in "╗╔╝╚║═":
            colored += LIGHT_COLOR + char + RESET
        else:
            colored += char
    return colored


def wrap_text(text: str, width: int, max_lines: int = 3) -> list[str]:
    """Wrap text into lines with hyphenation, truncate if exceeds max_lines."""
    if width <= 0:
        return [text[:50] + "..." if len(text) > 50 else text]

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if not current_line:
            if len(word) <= width:
                current_line = word
            else:
                # Word too long, hyphenate it
                while len(word) > width:
                    lines.append(word[: width - 1] + "-")
                    word = word[width - 1 :]
                current_line = word
        elif len(current_line) + 1 + len(word) <= width:
            current_line += " " + word
        else:
            # Fill remaining space with part of next word + hyphen
            remaining = width - len(current_line) - 1  # -1 for space
            if remaining >= 2:  # Need at least 1 char + hyphen
                current_line += " " + word[: remaining - 1] + "-"
                word = word[remaining - 1 :]
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    # Truncate if exceeds max_lines
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: width - 3] + "..."

    return lines


def make_banner() -> None:
    """Print the kudosx ASCII art banner."""
    banner_width = shutil.get_terminal_size().columns
    art_width = len(BASE_ART[0])
    available_width = banner_width - art_width - 2

    quote, author = random.choice(QUOTES)

    # Wrap quote into max 3 lines, leave 1 line for author
    quote_lines = wrap_text(quote, available_width, max_lines=3)
    quote_lines.append(f"—— {author}")

    term_width = shutil.get_terminal_size().columns

    for i, line in enumerate(BASE_ART):
        padding = " " * (term_width - len(line))
        if i == 1:
            text = f"{__package_name__} {GRAY_COLOR}v{__version__}"
            text_pad = " " * (term_width - len(line) - len(__package_name__) - len(f" v{__version__}") - 1)
            print(f"{BG_COLOR}{colorize(line)}{WHITE_COLOR}{text}{text_pad}{RESET}")
        elif i == 2:
            text = "· Powered by Claude Code"
            text_pad = " " * (term_width - len(line) - len(text) - 1)
            print(f"{BG_COLOR}{colorize(line)}{GRAY_COLOR}{text}{text_pad}{RESET}")
        elif i in (3, 4, 5, 6):
            quote_idx = i - 3
            if quote_idx < len(quote_lines):
                text = quote_lines[quote_idx]
                text_pad = " " * (term_width - len(line) - len(text) - 1)
                print(f"{BG_COLOR}{colorize(line)}{GRAY_COLOR}{ITALIC}{text}{RESET}{BG_COLOR}{text_pad}{RESET}")
            else:
                print(f"{BG_COLOR}{colorize(line)}{padding}{RESET}")
        else:
            print(f"{BG_COLOR}{colorize(line)}{padding}{RESET}")


if __name__ == "__main__":
    make_banner()
