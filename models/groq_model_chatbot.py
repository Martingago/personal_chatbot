#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import chromadb
from groq import Groq
from dotenv import load_dotenv 
import os


# In[ ]:


# Instance the APP VARIABLES
SYSTEM_PROMPT_PATH = "../system_prompt.txt"
CHROMA_DB = "../chromadb/persistent_db/"


# In[ ]:


chroma_client = chromadb.PersistentClient(path=CHROMA_DB)
collection = chroma_client.get_or_create_collection(
    name="cv_doc",
    metadata = {"hnsw:space": "cosine"}
)


# In[ ]:


class Chatbot:

    # Inits the basic atributes of the chatbot
    def __init__(self, system_prompt_path: str):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.system_prompt = self.read_doc(system_prompt_path) # init system_prompt
        self.context = self.system_prompt #init context
        self.documents = "" #init documents where data is extracted
        self.messages = [{"role": "system","content" : self.context}] #init of messages of the chat
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

    # Gets the user message > gets the context documents > append the user message to chat > updates system content
    def handle_user_query(self, user_message : str) :
        self.documents = self.get_context_query(user_message) # gets the new context
        self.context = self.system_prompt + self.documents # updates the new context for the model
        self.add_user_message(user_message) # adds the user message to the chat
        self.messages[0]['content'] = self.context # update the context message with the new context
    
    #Gets the embeddings context from user message
    def get_context_query(self, user_message : str) -> str :
        query_results = collection.query(
        query_texts = user_message,
        n_results= 3
        )
        context_entries = []  # Lista para almacenar las entradas del contexto

        # Recorre los documentos y metadatos obtenidos
        for doc, metadata in zip(query_results['documents'][0], query_results['metadatas'][0]):
            # Formatear el texto del documento y los metadatos
            context_entry = f'{{"data": "{doc}", "url_source": "{metadata.get("document", "N/A")}"}}'
            context_entries.append(context_entry)

        # Devuelve las entradas de contexto como una cadena
        print(context_entries)
        return str(context_entries)
        
    # Generates a iteration on the chat: add user and assistant messages to the history.
    def chat_iteration(self, user_message : str):
        self.handle_user_query(user_message)
        
        completion = self.get_completion()
        assistant_response = ""
        for chunk in completion:
            response_part = chunk.choices[0].delta.content or ""
            print(response_part, end="")
            assistant_response += response_part
        self.add_assistant_message(assistant_response)

    # Generates the chat funcion that allow users send multiple messages on a conversation
    def chat(self):
        while True:
            user_message = self.get_user_message()
            if user_message.strip().lower() == "/exit" :
                print("Hasta luego!")
                break
            self.chat_iteration(user_message) 


# In[ ]:


chatbot = Chatbot(SYSTEM_PROMPT_PATH)


# In[ ]:


chatbot.chat()

