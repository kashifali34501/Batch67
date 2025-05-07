# hello_agent/agent_hello.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client (you might not strictly need this for a simple print)
client = OpenAI(api_key=openai_api_key)

def my_first_agent():
    """
    This is a simple agent that prints a "Hello, world!" message.
    While it doesn't directly use the advanced features of the OpenAI Agent SDK
    for conversation or tools, it serves as a basic starting point within
    the required package structure.
    """
    print("Hello, world! This is your first OpenAI Agent SDK agent.")

if __name__ == "__main__":
    my_first_agent()