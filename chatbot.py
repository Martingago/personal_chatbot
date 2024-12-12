from groq import Groq
from dotenv import load_dotenv 
import os

class Chatbot:

    def __init__(self, system_prompt_path: str):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.system_prompt = self.read_doc(system_prompt_path)
        self.messages = [
            {"role": "system",
             "content" : self.system_prompt
             }
        ]
        self.client = Groq(api_key= self.api_key)

  
    # Gets the user input message
    def get_user_message(self):
        return input("Escribe tu mensaje: ")
    
    # Appends user message in the message history
    def add_user_message(self, message: str):
        self.messages.append({"role": "user", "content": message})
    
    # Add the role assistant to the message pool list.
    def add_assistant_message(self, message: str):
        self.messages.append({"role": "assistant", "content": message})

    # Reads the documents from the system
    def read_doc(self, path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    # Generates the model, params, and options    
    def get_completion(self):
        return self.client.chat.completions.create( 
            model="llama-3.1-8b-instant", 
            messages=self.messages, 
            temperature=1, 
            max_tokens=1024, 
            top_p=1, 
            stream=True,
            stop=None
        )
    
    # Generates a iteration on the chat: add user and assistant messages to the history.
    def chat_iteration(self, user_message : str):
        self.add_user_message(user_message)
        completion = self.get_completion()
        assistant_response = ""
        for chunk in completion:
            response_part = chunk.choices[0].delta.content or ""
            print(response_part, end="")
            assistant_response += response_part
        self.add_assistant_message(assistant_response)

    def chat(self):
        while True:
            user_message = self.get_user_message()
            if user_message.strip().lower() == "/exit" :
                print("Hasta luego!")
                break
            self.chat_iteration(user_message)  

if __name__ == "__main__": 
    system_prompt_path = "./system_prompt.txt" 
    chatbot = Chatbot(system_prompt_path)
    chatbot.chat()            
