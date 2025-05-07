# message_formatter/message_formatter.py

def backtick_border(func):
    """A decorator that adds a border of backticks around the message."""
    def wrapper(*args, **kwargs):
        message = func(*args, **kwargs)
        border = "`" * (len(message) + 4)
        return f"{border}\n` {message} `\n{border}"
    return wrapper

def code_emoji(func):
    """A decorator that adds code-related emojis before and after the message."""
    def wrapper(*args, **kwargs):
        message = func(*args, **kwargs)
        return f"💻💻💻💻 {message} 🚀🚀🚀🚀"
    return wrapper