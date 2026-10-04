import os
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN)

topic = input("Enter a topic: ")

prompt = f"""
Create 5 flashcards about {topic}.

For each flashcard, give:
Question:
Answer:

Keep the answers short and easy to understand.
"""
start_time =time.time()
response = client.chat_completion(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="meta-llama/Llama-3.1-8B-Instruct"
)

print("\nGenerated Flashcards:\n")
print(response.choices[0].message.content)
end_time = time.time()
print(response.choices[0].message.content)