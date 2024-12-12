from groq import Groq
from dotenv import load_dotenv 
import os

# Cargar el archivo .env
load_dotenv()

# Creates the instance of the client:
def read_doc(path: str):
    with open(path, 'r') as f:
        return f.read()


system_prompt = read_doc("./system_prompt.txt")

user_message = input("user message:")

client = Groq(
    api_key= os.getenv("GROQ_API_KEY")
)
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role" : "system",
         "content": system_prompt
         },
         {"role": "user",
          "content": user_message}
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


