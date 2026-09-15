from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

model = "gpt-4o"
zero_shot_msg = [
    {"role": "system", "content": "You are a cat. Answer like a cat."},
    {"role": "user", "content": "cat"}
]

one_shot_msg = [
    {"role": "system", "content": "You are a cat. Answer like a cat."},
    {"role": "user", "content": "cat"},
    {"role": "assistant", "content": "Meow"},
    {"role": "user", "content": "cat"}
]

few_shot_msg = [
    {"role": "system", "content": "You are a cat. Answer like a cat."},
    {"role": "user", "content": "cat"},
    {"role": "assistant", "content": "Meow"},
    {"role": "user", "content": "cat"},
    {"role": "assistant", "content": "Purr"},
        {"role": "user", "content": "cat"},
    {"role": "assistant", "content": "Meow meow"},
    {"role": "user", "content": "cat"}
]

zero_response = client.chat.completions.create(
    model=model,
    messages= zero_shot_msg,  
    temperature=0.9,  # Adjust temperature for creativity
)

one_response = client.chat.completions.create(
    model=model,
    messages= one_shot_msg,  
    temperature=0.9,  # Adjust temperature for creativity
)

few_response = client.chat.completions.create(
    model=model,
    messages= few_shot_msg,  
    temperature=0.9,  # Adjust temperature for creativity
)


print(zero_response.choices[0].message.content)
print(one_response.choices[0].message.content)
print(few_response.choices[0].message.content)