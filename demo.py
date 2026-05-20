from getpass import getpass
import numpy as np 
import pandas as pd 
import anthropic 
import openai 
import nltk 
nltk.download('vader_lexicon')
from sklearn.feature_extraction.text import CountVectorizer
from transformers import pipeline

# 1. Securely prompt the user for their API key
api_key_input = getpass("Enter your Anthropic API key: ")

# 2. Pass the inputted key to the client
client = anthropic.Anthropic(api_key=api_key_input)

# 3. Create and send the message
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

# 4. Print the response
print(message.content[0].text)