# main.py
from message_formatter.message_formatter import backtick_border, code_emoji

@backtick_border
@code_emoji
def display_message(text):
    """A function that returns a text message."""
    return text

if __name__ == "__main__":
    formatted_message = display_message("Hello, fellow coders!")
    print(formatted_message)

@code_emoji
def shout_out(text):
    """Another function to demonstrate a single decorator."""
    return f"HEY! {text.upper()}!"

if __name__ == "__main__":
    shouted_message = shout_out("python is awesome")
    print(shouted_message)