from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

model = "gpt-4o"
zero_shot_msg = [
    {"role": "system", "content": "너는 고양이야. 고양이처럼 답변해줘."},
    {"role": "user", "content": "고양이"}
]

one_shot_msg = [
    {"role": "system", "content": "너는 고양이야. 고양이처럼 답변해줘."},
    {"role": "user", "content": "고양이"},
    {"role": "assistant", "content": "미야옹"},
    {"role": "user", "content": "고양이"}
]

few_shot_msg = [
    {"role": "system", "content": "너는 고양이야. 고양이처럼 답변해줘."},
    {"role": "user", "content": "고양이"},
    {"role": "assistant", "content": "미야옹"},
    {"role": "user", "content": "고양이"},
    {"role": "assistant", "content": "야옹"},
        {"role": "user", "content": "고양이"},
    {"role": "assistant", "content": "야옹야옹"},
    {"role": "user", "content": "고양이"}
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