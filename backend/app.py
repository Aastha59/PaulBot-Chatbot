# import os 
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY: 
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins =["*"],
#     allow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"],
# )

# client = Groq(api_key=GROQ_API_KEY)

# class UserInput(BaseModel):
#     message : str
#     role : str ="user"
#     conversation_id : str

# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {"role": "system", "content":"You are a useful AI assistant."}
#         ]
#         self.active: bool = True

# # In-memory dictionary to hold active conversations during the app's runtime
# conversations: Dict[str,Conversation] = {}

# def query_groq_api(conversation: Conversation) ->str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=True, 
#             stop=None, 
#         )
#         response="" 
#         for chunk in completion:
#             response+=chunk.choices[0].delta.content or ""
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error with Groq API: {str(e)}")

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# @app.post("/chat/")
# async def chat(input: UserInput):
#     #Retrieve or create the conversation
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(
#             status_code=400,
#             detail="The chat session has ended. Please start a new session."
#         )
#     try:
#         #Append the user's message to the conversation
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })
#         response=query_groq_api(conversation)
#         conversation.messages.append({
#             "role":"assistant",
#             "content": response
#         })

#         return{
#             "response":response,
#             "conversation_id": input.conversation_id
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# if __name__ =="__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)






# import os
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware


# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")


# app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# client = Groq(api_key=GROQ_API_KEY)


# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str
    
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {"role": "system", "content": "You are a useful AI assistant."}
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}




# def query_groq_api(conversation: Conversation) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=True,
#             stop=None,
#         )
        
#         response = ""
#         for chunk in completion:
#             response += chunk.choices[0].delta.content or ""
        
#         return response
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error with Groq API: {str(e)}")


# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]




# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(
#             status_code=400, 
#             detail="The chat session has ended. Please start a new session."
#         )
        
#     try:
#         # Append the user's message to the conversation
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })
        
#         response = query_groq_api(conversation)
        
#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })
        
#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)





# import os
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # Load environment variables from .env
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # Initialize FastAPI app
# app = FastAPI()

# # Add CORS middleware to allow frontend requests
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Groq client
# client = Groq(api_key=GROQ_API_KEY)

# # Request body model
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # Class to manage each conversation
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {"role": "system", "content": "You are a useful AI assistant."}
#         ]
#         self.active: bool = True

# # Store active conversations
# conversations: Dict[str, Conversation] = {}

# # Get or create a conversation instance
# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# # Query Groq API and return response
# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#             stop=None,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             if not response.strip():
#                 raise HTTPException(status_code=500, detail="No content received from streaming.")
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error with Groq API: {str(e)}")

# # Root route for testing
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# # Chat endpoint
# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(
#             status_code=400,
#             detail="The chat session has ended. Please start a new session."
#         )

#     try:
#         # Add user's message to conversation history
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Query Groq API (you can toggle `stream=True` if needed)
#         response = query_groq_api(conversation, stream=False)

#         # Add assistant's response
#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Entry point for running with `python app.py`
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)









# import os
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware
# import PyPDF2  # For PDF reading

# # Load environment variables
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # === PDF Extraction ===
# def extract_pdf_text(pdf_path):
#     text = ""
#     with open(pdf_path, "rb") as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             content = page.extract_text()
#             if content:
#                 text += content + "\n"
#     return text

# # Load PDF content once at startup
# PDF_CONTEXT = extract_pdf_text("Pml_queries.pdf")

# # === FastAPI app ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# client = Groq(api_key=GROQ_API_KEY)

# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # Store conversation context
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a helpful AI assistant. Below is important information about Paul Merchants.\n\n"
#                     f"{PDF_CONTEXT[:2000]}"  # Truncate if needed
#                 )
#             }
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# # Groq call
# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#             stop=None,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             if not response.strip():
#                 raise HTTPException(status_code=500, detail="No content received from streaming.")
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error with Groq API: {str(e)}")

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(
#             status_code=400,
#             detail="The chat session has ended. Please start a new session."
#         )

#     try:
#         # User input
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Model response
#         response = query_groq_api(conversation)

#         # Store response
#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Run
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)











# import os
# import fitz  # PyMuPDF
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load Environment Variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # === Load PDF Content ===
# PDF_PATH = "Pml_queries.pdf"

# def extract_text_from_pdf(path: str) -> str:
#     try:
#         with fitz.open(path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#             return text
#     except Exception as e:
#         print("❌ Error reading PDF:", e)
#         return ""

# pdf_context = extract_text_from_pdf(PDF_PATH)
# TRUNCATED_PDF_CONTEXT = pdf_context[:2000]  # Keep it concise to avoid token overflow

# if TRUNCATED_PDF_CONTEXT.strip():
#     print("✅ PDF loaded successfully.")
# else:
#     print("❌ Failed to load or extract text from PDF.")

# # === FastAPI App Setup ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# client = Groq(api_key=GROQ_API_KEY)

# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. You are informed by the following context extracted from a PDF:\n\n{TRUNCATED_PDF_CONTEXT}"
#             }
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#             stop=None,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error with Groq API: {str(e)}")

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(status_code=400, detail="The chat session has ended. Please start a new session.")

#     try:
#         # Append user message
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Query Groq with context
#         response = query_groq_api(conversation, stream=False)

#         # Save assistant reply
#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Run with: python app.py
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)





# 653


# import os
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # === Load knowledge context from text file ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === Initialize FastAPI ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq client ===
# client = Groq(api_key=GROQ_API_KEY)

# # === Request model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === Conversation memory ===
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants while replying:\n\n{context_text}"
#             }
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#             stop=None,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             if not response.strip():
#                 raise HTTPException(status_code=500, detail="No content received.")
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")

# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(status_code=400, detail="Session has ended. Please start a new one.")

#     try:
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         response = query_groq_api(conversation, stream=False)

#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # === Run if executed directly ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)











# import os
# import streamlit as st
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationEntityMemory
# from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
# from langchain.llms import OpenAI 

# # === Load environment variables ===

# #Initialize session states
# if "generated" not in st.session_state:
#     st.session_state["generated"] = [] #output
# if "past" not in st.session_state:
#     st.session_state["past"] = [] #past
# if "input" not in st.session_state:
#     st.session_state["input"] = ""
# if "stored_session" not in st.session_state:
#     st.session_state["stored_session"] = []

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # === Load knowledge context from text file ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === Initialize FastAPI ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq client ===
# client = Groq(api_key=GROQ_API_KEY)

# # === Request model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === Conversation memory ===
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants while replying:\n\n{context_text}"
#             }
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#             stop=None,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             if not response.strip():
#                 raise HTTPException(status_code=500, detail="No content received.")
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")

# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(status_code=400, detail="Session has ended. Please start a new one.")

#     try:
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         response = query_groq_api(conversation, stream=False)

#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # === Run if executed directly ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
 



# unified_bot.py

# import os
# from typing import List, Dict
# from dotenv import load_dotenv

# # === FastAPI ===
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from groq import Groq

# # === Streamlit + LangChain ===
# import streamlit as st
# from langchain_community.llms import OpenAI
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationEntityMemory
# from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

# # === Load Environment Variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY not found in environment. Please define it in .env.")

# # === Load Context for FastAPI Memory ===
# CONTEXT_FILE = "Pml_queries.txt"
# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"[!] Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === Groq Client ===
# groq_client = Groq(api_key=GROQ_API_KEY)

# # === FastAPI App Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === In-memory storage for conversations ===
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use this knowledge about Paul Merchants:\n\n{context_text}"
#             }
#         ]
#         self.active = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# def query_groq(conversation: Conversation) -> str:
#     try:
#         completion = groq_client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=False,
#         )
#         return completion.choices[0].message.content.strip()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")

# # === FastAPI Routes ===
# @app.get("/")
# def root():
#     return {"message": "Welcome to PaulBot API!"}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)
#     if not conversation.active:
#         raise HTTPException(status_code=400, detail="Session ended. Please start a new one.")

#     conversation.messages.append({"role": input.role, "content": input.message})
#     response = query_groq(conversation)
#     conversation.messages.append({"role": "assistant", "content": response})

#     return {"response": response, "conversation_id": input.conversation_id}

# # ============================
# # === Streamlit UI App =======
# # ============================

# def run_streamlit():
#     st.set_page_config(page_title='🧠MemoryBot🤖', layout='wide')

#     # Session states
#     for key in ["generated", "past", "input", "stored_session"]:
#         if key not in st.session_state:
#             st.session_state[key] = [] if key != "input" else ""

#     def get_text():
#         return st.text_input("You: ", st.session_state["input"], key="input",
#                              placeholder="Your AI assistant here! Ask me anything ...", 
#                              label_visibility='hidden')

#     def new_chat():
#         save = []
#         for i in range(len(st.session_state['generated'])-1, -1, -1):
#             save.append("User:" + st.session_state["past"][i])
#             save.append("Bot:" + st.session_state["generated"][i])
#         st.session_state["stored_session"].append(save)
#         st.session_state["generated"] = []
#         st.session_state["past"] = []
#         st.session_state["input"] = ""
#         st.session_state.entity_memory.entity_store = {}
#         st.session_state.entity_memory.buffer.clear()

#     # Sidebar
#     with st.sidebar.expander("🛠️", expanded=False):
#         if st.checkbox("Preview memory store"):
#             with st.expander("Memory Store"):
#                 st.write(st.session_state.entity_memory.store)

#         if st.checkbox("Preview memory buffer"):
#             with st.expander("Buffer"):
#                 st.write(st.session_state.entity_memory.buffer)

#         model_name = st.selectbox("Model", options=["gpt-3.5-turbo", "text-davinci-003"])
#         K = st.number_input("Summary of past messages to consider (K)", min_value=3, max_value=1000)

#     st.title("🤖 Chat Bot with 🧠")
#     st.subheader("Powered by 🦜 LangChain + OpenAI + Streamlit")

#     api_key = st.sidebar.text_input("OpenAI API Key", type="password")

#     if api_key:
#         llm = OpenAI(temperature=0, openai_api_key=api_key, model_name=model_name, verbose=False)

#         if "entity_memory" not in st.session_state:
#             st.session_state.entity_memory = ConversationEntityMemory(llm=llm, k=K)

#         conversation_chain = ConversationChain(
#             llm=llm,
#             prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
#             memory=st.session_state.entity_memory
#         )

#         st.sidebar.button("New Chat", on_click=new_chat, type="primary")
#         user_input = get_text()

#         if user_input:
#             output = conversation_chain.run(input=user_input)
#             st.session_state.past.append(user_input)
#             st.session_state.generated.append(output)

#         # Display conversation
#         with st.expander("Conversation", expanded=True):
#             chat_export = []
#             for i in range(len(st.session_state['generated'])-1, -1, -1):
#                 st.info(st.session_state["past"][i], icon="🧐")
#                 st.success(st.session_state["generated"][i], icon="🤖")
#                 chat_export.append(st.session_state["past"][i])
#                 chat_export.append(st.session_state["generated"][i])
#             if chat_export:
#                 st.download_button("Download", '\n'.join(chat_export))

#         # Stored sessions
#         for i, sess in enumerate(st.session_state.stored_session):
#             with st.sidebar.expander(f"Session {i}"):
#                 st.write(sess)

#         if st.session_state.stored_session:
#             if st.sidebar.checkbox("Clear All"):
#                 del st.session_state.stored_session

#     else:
#         st.sidebar.warning("⚠️ Please enter your OpenAI API key to start.")

# # === Entry Point ===
# if __name__ == "__main__":
#     import sys
#     if "streamlit" in sys.argv[0]:
#         run_streamlit()
#     else:
#         import uvicorn
#         uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)











# import os
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# import streamlit as st
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationEntityMemory
# from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
# # from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# if "generated" not in st.session_state:
#     st.session_state["generated"] = []
# if "past" not in st.session_state:
#     st.session_state["past"] = []
# if "input" not in st.session_state:
#     st.session_state["input"] = ""
# if "stored_session" not in st.session_state:
#     st.session_state["stored_session"] = []

# # === Load knowledge context from text file ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === Initialize FastAPI ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq client ===
# client = Groq(api_key=GROQ_API_KEY)

# # # === Request model ===
# # class UserInput(BaseModel):
# #     message: str
# #     role: str = "user"
# #     conversation_id: str

# # # === Conversation memory ===
# # class Conversation:
# #     def __init__(self):
# #         self.messages: List[Dict[str, str]] = [
# #             {
# #                 "role": "system",
# #                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants while replying:\n\n{context_text}"
# #             }
# #         ]
# #         self.active: bool = True

# # conversations: Dict[str, Conversation] = {}

# # def get_or_create_conversation(conversation_id: str) -> Conversation:
# #     if conversation_id not in conversations:
# #         conversations[conversation_id] = Conversation()
# #     return conversations[conversation_id]


# def get_text():
#     """
#     Get the user input text.

#     Returns:
#         (str): The text entered by the user
#     """
#     input_text = st.text_input("You: ", st.session_state["input"], key="input",
#                             placeholder="Your AI assistant here! Ask me anything ...", 
#                             label_visibility='hidden')
#     return input_text

# # Define function to start a new chat
# def new_chat():
#     """
#     Clears session state and starts a new chat.
#     """
#     save = []
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         save.append("User:" + st.session_state["past"][i])
#         save.append("Bot:" + st.session_state["generated"][i])        
#     st.session_state["stored_session"].append(save)
#     st.session_state["generated"] = []
#     st.session_state["past"] = []
#     st.session_state["input"] = ""
#     st.session_state.entity_memory.entity_store = {}
#     st.session_state.entity_memory.buffer.clear()

# # Set up sidebar with various options
# with st.sidebar.expander("🛠️ ", expanded=False):
#     # Option to preview memory store
#     if st.checkbox("Preview memory store"):
#         with st.expander("Memory-Store", expanded=False):
#             st.session_state.entity_memory.store
#     # Option to preview memory buffer
#     if st.checkbox("Preview memory buffer"):
#         with st.expander("Bufffer-Store", expanded=False):
#             st.session_state.entity_memory.buffer
#     MODEL = st.selectbox(label='Model', options=['gpt-3.5-turbo','text-davinci-003','text-davinci-002','code-davinci-002'])
#     K = st.number_input(' (#)Summary of prompts to consider',min_value=3,max_value=1000)


# # def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
# #     try:
# #         completion = client.chat.completions.create(
# #             model="llama-3.1-8b-instant",
# #             messages=conversation.messages,
# #             temperature=1,
# #             max_tokens=1024,
# #             top_p=1,
# #             stream=stream,
# #             stop=None,
# #         )

# #         if stream:
# #             response = ""
# #             for chunk in completion:
# #                 delta = chunk.choices[0].delta
# #                 if delta and delta.content:
# #                     response += delta.content
# #             if not response.strip():
# #                 raise HTTPException(status_code=500, detail="No content received.")
# #             return response
# #         else:
# #             return completion.choices[0].message.content.strip()

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")





# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# # @app.post("/chat/")
# # async def chat(input: UserInput):
# #     conversation = get_or_create_conversation(input.conversation_id)

# #     if not conversation.active:
# #         raise HTTPException(status_code=400, detail="Session has ended. Please start a new one.")

# #     try:
# #         conversation.messages.append({
# #             "role": input.role,
# #             "content": input.message
# #         })

# #         response = query_groq_api(conversation, stream=False)

# #         conversation.messages.append({
# #             "role": "assistant",
# #             "content": response
# #         })

# #         return {
# #             "response": response,
# #             "conversation_id": input.conversation_id
# #         }

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # Ask the user to enter their OpenAI API key
# API_O = st.sidebar.text_input("API-KEY", type="password")

# # Session state storage would be ideal
# if API_O:
#     # Create an OpenAI instance
#     llm = OpenAI(temperature=0,
#                 openai_api_key=API_O, 
#                 model_name=MODEL, 
#                 verbose=False) 


#     # Create a ConversationEntityMemory object if not already created
#     if 'entity_memory' not in st.session_state:
#             st.session_state.entity_memory = ConversationEntityMemory(llm=llm, k=K )
        
#         # Create the ConversationChain object with the specified configuration
#     Conversation = ConversationChain(
#             llm=llm, 
#             prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
#             memory=st.session_state.entity_memory
#         )  
# else:
#     st.sidebar.warning('API key required to try this app.The API key is not stored in any form.')
#     # st.stop()


# # Add a button to start a new chat
# st.sidebar.button("New Chat", on_click = new_chat, type='primary')

# # Get the user input
# user_input = get_text()

# # Generate the output using the ConversationChain object and the user input, and add the input/output to the session
# if user_input:
#     output = Conversation.run(input=user_input)  
#     st.session_state.past.append(user_input)  
#     st.session_state.generated.append(output)  

# # Allow to download as well
# download_str = []
# # Display the conversation history using an expander, and allow the user to download it
# with st.expander("Conversation", expanded=True):
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         st.info(st.session_state["past"][i],icon="🧐")
#         st.success(st.session_state["generated"][i], icon="🤖")
#         download_str.append(st.session_state["past"][i])
#         download_str.append(st.session_state["generated"][i])
    
#     # Can throw error - requires fix
#     download_str = '\n'.join(download_str)
#     if download_str:
#         st.download_button('Download',download_str)

# # Display stored conversation sessions in the sidebar
# for i, sublist in enumerate(st.session_state.stored_session):
#         with st.sidebar.expander(label= f"Conversation-Session:{i}"):
#             st.write(sublist)

# # Allow the user to clear all stored conversation sessions
# if st.session_state.stored_session:   
#     if st.sidebar.checkbox("Clear-all"):
#         del st.session_state.stored_session

# # === Run if executed directly ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)









# import os
# import json
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # === Load knowledge context from text file ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === Initialize FastAPI ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq client ===
# client = Groq(api_key=GROQ_API_KEY)

# # === Request model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === Conversation memory ===
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants while replying:\n\n{context_text}"
#             }
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#             stop=None,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             if not response.strip():
#                 raise HTTPException(status_code=500, detail="No content received.")
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")

# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     conversation = get_or_create_conversation(input.conversation_id)

#     if not conversation.active:
#         raise HTTPException(status_code=400, detail="Session has ended. Please start a new one.")

#     try:
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         response = query_groq_api(conversation, stream=False)

#         conversation.messages.append({
#             "role": "assistant",
#             "content": response
#         })

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # === Run if executed directly ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# import os
# import json
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY missing in .env")

# if not MONGO_URI:
#     raise ValueError("MONGODB_URI missing in .env")

# # === MongoDB Setup ===
# client = MongoClient(MONGO_URI)
# db = client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load knowledge context ===
# CONTEXT_FILE = "Pml_queries.txt"
# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq LLM Client ===
# client_llm = Groq(api_key=GROQ_API_KEY)

# # === Request model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === MongoDB Memory ===
# def save_message(conversation_id: str, role: str, content: str):
#     doc = {
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     }
#     collection.insert_one(doc)

# def load_conversation(conversation_id: str):
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Conversation Object ===
# class Conversation:
#     def __init__(self, conversation_id: str):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
#             }
#         ]
#         self.messages += load_conversation(conversation_id)
#         self.active: bool = True

# def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
#     try:
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#             stream=stream,
#         )

#         if stream:
#             response = ""
#             for chunk in completion:
#                 delta = chunk.choices[0].delta
#                 if delta and delta.content:
#                     response += delta.content
#             if not response.strip():
#                 raise HTTPException(status_code=500, detail="No content received.")
#             return response
#         else:
#             return completion.choices[0].message.content.strip()

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")

# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     if not input.conversation_id:
#         raise HTTPException(status_code=400, detail="conversation_id is required")

#     conversation = Conversation(input.conversation_id)

#     conversation.messages.append({
#         "role": input.role,
#         "content": input.message
#     })

#     try:
#         response = query_groq_api(conversation)

#         # Save both user input and bot response to MongoDB
#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # === Run if executed directly ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)







# import os
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY missing in .env")

# if not MONGO_URI:
#     raise ValueError("MONGODB_URI missing in .env")

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load knowledge context ===
# CONTEXT_FILE = "Pml_queries.txt"
# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq LLM Client ===
# client_llm = Groq(api_key=GROQ_API_KEY)

# # === Request model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === MongoDB Memory Utilities ===
# def save_message(conversation_id: str, role: str, content: str):
#     doc = {
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     }
#     collection.insert_one(doc)

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         # Load previous messages
#         messages = load_conversation(input.conversation_id)

#         # Add system prompt only once
#         if not any(msg["role"] == "system" for msg in messages):
#             messages.insert(0, {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
#             })

#         # Add current user message
#         messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Query Groq API
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#         )
#         response = completion.choices[0].message.content.strip()

#         # Save both messages
#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# # === Run server ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# # === Validate environment variables ===
# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load knowledge context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq LLM Client ===
# client_llm = Groq(api_key=GROQ_API_KEY)

# # === Pydantic Model for Request ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === MongoDB Memory Utilities ===
# def save_message(conversation_id: str, role: str, content: str):
#     doc = {
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     }
#     collection.insert_one(doc)

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Routes ===

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         # Load previous conversation
#         messages = load_conversation(input.conversation_id)

#         # Add system prompt only once
#         if not any(msg["role"] == "system" for msg in messages):
#             messages.insert(0, {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
#             })

#         # Add current user message
#         messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Query Groq API
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#         )
#         response = completion.choices[0].message.content.strip()

#         # Save conversation
#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         traceback.print_exc()  # Show full traceback in terminal
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# # @app.post("/chat/")
# # async def chat(input: UserInput):
# #     try:
# #         print(f"[DEBUG] Received message: {input.message}")
# #         print(f"[DEBUG] Conversation ID: {input.conversation_id}")

# #         # Load previous conversation
# #         messages = load_conversation(input.conversation_id)
# #         print(f"[DEBUG] Loaded {len(messages)} previous messages.")

# #         # Add system prompt only once
# #         if not any(msg["role"] == "system" for msg in messages):
# #             print("[DEBUG] Adding system prompt.")
# #             messages.insert(0, {
# #                 "role": "system",
# #                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
# #             })

# #         # Add current user message
# #         messages.append({
# #             "role": input.role,
# #             "content": input.message
# #         })
# #         print("[DEBUG] Final messages to LLM:")
# #         for msg in messages:
# #             print(f" - {msg['role']}: {msg['content'][:50]}...")

# #         # Query Groq API
# #         completion = client_llm.chat.completions.create(
# #             model="llama-3.1-8b-instant",
# #             messages=messages,
# #             temperature=1,
# #             max_tokens=1024,
# #             top_p=1,
# #         )

# #         response = completion.choices[0].message.content.strip()
# #         print(f"[DEBUG] LLM Response: {response[:100]}...")

# #         # Save conversation
# #         save_message(input.conversation_id, input.role, input.message)
# #         save_message(input.conversation_id, "assistant", response)

# #         return {
# #             "response": response,
# #             "conversation_id": input.conversation_id
# #         }

# #     except Exception as e:
# #         print("❌ Exception occurred:")
# #         import traceback
# #         traceback.print_exc()
# #         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


# # === Run server manually if needed ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# import os
# import traceback
# from typing import List, Dict
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")
# LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.1-8b-instant")

# # === Validate environment variables ===
# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === MongoDB Setup ===
# try:
#     mongo_client = MongoClient(MONGO_URI)
#     db = mongo_client[DB_NAME]
#     collection = db[COLLECTION_NAME]
# except Exception as e:
#     raise RuntimeError(f"❌ Failed to connect to MongoDB: {e}")

# # === Load context (knowledge base) ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # ⚠️ For production, restrict origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq LLM Setup ===
# client_llm = Groq(api_key=GROQ_API_KEY)

# # === Pydantic Schema ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === MongoDB Utilities ===
# def save_message(conversation_id: str, role: str, content: str):
#     try:
#         doc = {
#             "conversation_id": conversation_id,
#             "role": role,
#             "content": content,
#             "timestamp": datetime.utcnow()
#         }
#         collection.insert_one(doc)
#     except Exception as e:
#         print(f"❌ MongoDB insert error: {e}")

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     try:
#         messages = list(collection.find(
#             {"conversation_id": conversation_id},
#             sort=[("timestamp", 1)]
#         ))
#         return [{"role": m["role"], "content": m["content"]} for m in messages]
#     except Exception as e:
#         print(f"❌ MongoDB fetch error: {e}")
#         return []

# # === Routes ===
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         print(f"[DEBUG] Message: {input.message}")
#         print(f"[DEBUG] Conversation ID: {input.conversation_id}")

#         # Validate input length
#         if len(input.message) > 1000:
#             raise HTTPException(status_code=400, detail="❌ Input too long. Limit to 1000 characters.")

#         # Load prior messages
#         messages = load_conversation(input.conversation_id)

#         # Inject system prompt only once
#         if not any(msg["role"] == "system" for msg in messages):
#             messages.insert(0, {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
#             })

#         # Add current user message
#         messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         print("[DEBUG] Messages prepared for LLM:")
#         for msg in messages:
#             print(f" - {msg['role']}: {msg['content'][:60]}...")

#         # Query Groq LLM
#         completion = client_llm.chat.completions.create(
#             model=LLM_MODEL,
#             messages=messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#         )
#         response = completion.choices[0].message.content.strip()
#         print(f"[DEBUG] LLM Response: {response[:100]}...")

#         # Save conversation to MongoDB
#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"❌ Internal Server Error: {str(e)}")

# # === For local run ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# import os
# from typing import List, Dict
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# import openai

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# # === Configure OpenAI Client to Use Groq ===
# openai.api_key = GROQ_API_KEY
# openai.api_base = "https://api.groq.com/openai/v1"

# # === Load knowledge context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Pydantic Model for User Request ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === In-Memory Conversation Store ===
# class Conversation:
#     def __init__(self):
#         self.messages: List[Dict[str, str]] = [
#             {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants while replying:\n\n{context_text}"
#             }
#         ]
#         self.active: bool = True

# conversations: Dict[str, Conversation] = {}

# def get_or_create_conversation(conversation_id: str) -> Conversation:
#     if conversation_id not in conversations:
#         conversations[conversation_id] = Conversation()
#     return conversations[conversation_id]

# # === Route Handlers ===
# @app.get("/")
# def read_root():
#     return {"message": "✅ PaulBot API is running. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         conversation = get_or_create_conversation(input.conversation_id)

#         if not conversation.active:
#             raise HTTPException(status_code=400, detail="Session has ended. Start a new one.")

#         # Add user message to memory
#         conversation.messages.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Query Groq (using OpenAI-style call)
#         response_data = openai.ChatCompletion.create(
#             model="llama-3-8b-8192",  # Replace with available Groq model
#             messages=conversation.messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1
#         )

#         response_text = response_data.choices[0].message.content.strip()

#         # Save assistant response to memory
#         conversation.messages.append({
#             "role": "assistant",
#             "content": response_text
#         })

#         return {
#             "response": response_text,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         import traceback
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

# # === Run the API server ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# # === Validate environment variables ===
# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load knowledge context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq LLM Client ===
# client_llm = Groq(api_key=GROQ_API_KEY)

# # === Pydantic Model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === MongoDB Helpers ===
# def save_message(conversation_id: str, role: str, content: str):
#     doc = {
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     }
#     collection.insert_one(doc)

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization Function ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         summary_prompt = [
#             {"role": "system", "content": "Summarize the following conversation briefly."},
#             *messages
#         ]
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=summary_prompt,
#             temperature=0.5,
#             max_tokens=500,
#             top_p=1,
#         )
#         return completion.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#         return "[Summary unavailable]"

# # === Routes ===

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}


# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         # Add system context only once
#         if not any(msg["role"] == "system" for msg in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # === Summarize if total character length is too long ===
#         total_characters = sum(len(m["content"]) for m in full_history)

#         if total_characters > 10000:
#             summary = await summarize_messages(full_history[:-10])
#             messages = [
#                 {
#                     "role": "system",
#                     "content": f"Summary of prior conversation:\n{summary}\n\nUse this summary along with the latest messages to continue helping the user."
#                 }
#             ] + full_history[-10:]
#         else:
#             messages = full_history

#         # Query LLM
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#         )
#         response = completion.choices[0].message.content.strip()

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")



# # @app.post("/chat/")
# # async def chat(input: UserInput):
# #     try:
# #         # Load full chat history
# #         full_history = load_conversation(input.conversation_id)

# #         # Add system context only once
# #         if not any(msg["role"] == "system" for msg in full_history):
# #             full_history.insert(0, {
# #                 "role": "system",
# #                 "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants:\n\n{context_text}"
# #             })

# #         # Add current user input
# #         full_history.append({
# #             "role": input.role,
# #             "content": input.message
# #         })

# #         # === Summarize old history if it's too long ===
# #         if len(full_history) > 25:
# #             summary = await summarize_messages(full_history[:-10])
# #             messages = [{
# #                 "role": "system",
# #                 "content": f"Summary of prior conversation:\n{summary}\n\nContinue the conversation below."
# #             }] + full_history[-10:]
# #         else:
# #             messages = full_history

# #         # Query Groq LLM
# #         completion = client_llm.chat.completions.create(
# #             model="llama-3.1-8b-instant",
# #             messages=messages,
# #             temperature=1,
# #             max_tokens=1024,
# #             top_p=1,
# #         )
# #         response = completion.choices[0].message.content.strip()

# #         # Save both user input and LLM response
# #         save_message(input.conversation_id, input.role, input.message)
# #         save_message(input.conversation_id, "assistant", response)

# #         return {
# #             "response": response,
# #             "conversation_id": input.conversation_id
# #         }

# #     except Exception as e:
# #         traceback.print_exc()
# #         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# # === Run if main ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# RUNNING 

# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment variables ===
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# # === Validate environment variables ===
# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load knowledge context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             return f.read()[:max_chars]
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)
# print("📄 Loaded context (first 200 chars):", context_text[:200])

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Groq LLM Client ===
# client_llm = Groq(api_key=GROQ_API_KEY)

# # === Pydantic Model ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# # === MongoDB Helpers ===
# def save_message(conversation_id: str, role: str, content: str):
#     doc = {
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     }
#     collection.insert_one(doc)

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization Function ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         summary_prompt = [
#             {"role": "system", "content": "Summarize the following conversation in a short bullet-point form."},
#             *messages
#         ]
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=summary_prompt,
#             temperature=0.3,
#             max_tokens=400,  # Reduced for compact summary
#             top_p=1,
#         )
#         return completion.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#         return "[Summary unavailable]"

# # === Routes ===

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the PaulBot API. Use POST /chat/ to chat."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         # Add current user input to history
#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         # Compute total character count of full conversation
#         total_characters = sum(len(m["content"]) for m in full_history)

#         # If long, summarize earlier part and use only last 10 exchanges + context
#         if total_characters > 10000:
#             summary = await summarize_messages(full_history[:-10])
#             messages = [
#                 {
#                     "role": "system",
#                     "content": f"""You are a helpful assistant for Paul Merchants.

# Here is your knowledge base:\n\n{context_text}

# Summary of prior conversation:\n{summary}

# Now continue the conversation below."""
#                 }
#             ] + full_history[-10:]
#         else:
#             # Add context only once
#             if not any(msg["role"] == "system" for msg in full_history):
#                 full_history.insert(0, {
#                     "role": "system",
#                     "content": f"You are a helpful assistant for Paul Merchants.\n\nUse the following knowledge base:\n\n{context_text}"
#                 })
#             messages = full_history

#         # Query LLM
#         completion = client_llm.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=messages,
#             temperature=1,
#             max_tokens=1024,
#             top_p=1,
#         )
#         response = completion.choices[0].message.content.strip()

#         # Save messages
#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# # === Main Runner ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)







# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from openai import OpenAI
# from fastapi.middleware.cors import CORSMiddleware

# # === Load environment ===
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not OPENAI_API_KEY:
#     raise ValueError("❌ OPENAI_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === OpenAI client ===
# client_llm = OpenAI(api_key=OPENAI_API_KEY)

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             context = f.read()[:max_chars]
#             print("📄 Loaded context (first 200 chars):", context[:200])
#             return context
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# def save_message(conversation_id: str, role: str, content: str):
#     collection.insert_one({
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     })

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         summary_prompt = [
#             {"role": "system", "content": "Summarize this conversation in short, meaningful bullet points."},
#             *messages
#         ]
#         completion = client_llm.chat.completions.create(
#             model="gpt-3.5-turbo",  # Use fallback for summarization
#             messages=summary_prompt,
#             max_tokens=400,
#             temperature=0.3
#         )
#         return completion.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#         return "[Summary unavailable]"

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to PaulBot. Use POST /chat/ to talk."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         if not any(m["role"] == "system" for m in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         total_chars = sum(len(m["content"]) for m in full_history)

#         if total_chars > 12000:
#             try:
#                 summary = await summarize_messages(full_history[:-10])
#             except Exception as summary_error:
#                 summary = "[Summary unavailable due to API issue]"
#                 print("⚠️ Summarization fallback:", summary_error)

#             messages = [{
#                 "role": "system",
#                 "content": f"Summary of previous conversation:\n{summary}\n\nNow continue helping the user based on the summary and recent messages."
#             }] + full_history[-10:]
#         else:
#             messages = full_history

#         # Try GPT-4, fallback to GPT-3.5, handle quota error gracefully
#         for model in ["gpt-4-0125-preview", "gpt-3.5-turbo"]:
#             try:
#                 completion = client_llm.chat.completions.create(
#                     model=model,
#                     messages=messages,
#                     max_tokens=1000,
#                     temperature=1,
#                 )
#                 break  # ✅ Success, exit loop
#             except Exception as e:
#                 if "insufficient_quota" in str(e):
#                     print("❌ Quota exhausted.")
#                     return {
#                         "response": "❌ OpenAI API quota exceeded. Please check your key or try again later.",
#                         "conversation_id": input.conversation_id
#                     }
#                 elif "model_not_found" in str(e):
#                     print(f"⚠️ Model {model} not available, trying fallback...")
#                     continue
#                 else:
#                     raise e

#         response = completion.choices[0].message.content.strip()

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", response)

#         return {
#             "response": response,
#             "conversation_id": input.conversation_id
#         }

#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")


# # @app.post("/chat/")
# # async def chat(input: UserInput):
# #     try:
# #         full_history = load_conversation(input.conversation_id)

# #         if not any(m["role"] == "system" for m in full_history):
# #             full_history.insert(0, {
# #                 "role": "system",
# #                 "content": f"""You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"""
# #             })

# #         full_history.append({
# #             "role": input.role,
# #             "content": input.message
# #         })

# #         total_chars = sum(len(m["content"]) for m in full_history)

# #         if total_chars > 12000:
# #             summary = await summarize_messages(full_history[:-10])
# #             messages = [{
# #                 "role": "system",
# #                 "content": f"""Summary of previous conversation:\n{summary}\n\nNow continue helping the user based on the summary and recent messages."""
# #             }] + full_history[-10:]
# #         else:
# #             messages = full_history

# #         try:
# #             # Try GPT-4 first
# #             completion = client_llm.chat.completions.create(
# #                 model="gpt-4-0125-preview",
# #                 messages=messages,
# #                 max_tokens=1000,
# #                 temperature=1,
# #             )
# #         except Exception as e:
# #             print("⚠️ GPT-4 model failed. Falling back to GPT-3.5. Error:", str(e))
# #             completion = client_llm.chat.completions.create(
# #                 model="gpt-3.5-turbo",
# #                 messages=messages,
# #                 max_tokens=1000,
# #                 temperature=1,
# #             )

# #         response = completion.choices[0].message.content.strip()

# #         save_message(input.conversation_id, input.role, input.message)
# #         save_message(input.conversation_id, "assistant", response)

# #         return {
# #             "response": response,
# #             "conversation_id": input.conversation_id
# #         }

# #     except Exception as e:
# #         traceback.print_exc()
# #         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# # === Run Server ===
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)










# GEMINI

# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# import google.generativeai as genai

# # === Load environment ===
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not GEMINI_API_KEY:
#     raise ValueError("❌ GEMINI_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === Gemini client ===
# genai.configure(api_key=GEMINI_API_KEY)
# # model_gemini = genai.GenerativeModel("gemini-pro")
# model_gemini = genai.GenerativeModel(model_name="models/gemini-pro")


# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             context = f.read()[:max_chars]
#             print("📄 Loaded context (first 200 chars):", context[:200])
#             return context
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# def save_message(conversation_id: str, role: str, content: str):
#     collection.insert_one({
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     })

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         prompt = "Summarize the following chat history in concise bullet points:\n"
#         for m in messages:
#             prompt += f"{m['role'].capitalize()}: {m['content']}\n"
#         response = model_gemini.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#         return "[Summary unavailable]"

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to PaulBot (Gemini). Use POST /chat/ to talk."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         if not any(m["role"] == "system" for m in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         total_chars = sum(len(m["content"]) for m in full_history)

#         if total_chars > 12000:
#             try:
#                 summary = await summarize_messages(full_history[:-10])
#             except Exception as summary_error:
#                 summary = "[Summary unavailable due to API issue]"
#                 print("⚠️ Summarization fallback:", summary_error)

#             prompt = f"Summary of previous conversation:\n{summary}\n\nRecent messages:\n"
#             for msg in full_history[-10:]:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
#         else:
#             prompt = ""
#             for msg in full_history:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

#         response = model_gemini.generate_content(prompt)
#         reply = response.text.strip()

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", reply)

#         return {
#             "response": reply,
#             "conversation_id": input.conversation_id
#         }

#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)






#CLAUDE

# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# import anthropic

# # === Load environment ===
# load_dotenv()
# CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not CLAUDE_API_KEY:
#     raise ValueError("❌ CLAUDE_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === Claude client ===
# client_claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             context = f.read()[:max_chars]
#             print("📄 Loaded context (first 200 chars):", context[:200])
#             return context
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# def save_message(conversation_id: str, role: str, content: str):
#     collection.insert_one({
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     })

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         chat_prompt = "".join([f"{m['role'].capitalize()}: {m['content']}\n" for m in messages])
#         msg = client_claude.messages.create(
#             model="claude-3-opus-20240229",
#             max_tokens=400,
#             temperature=0.3,
#             messages=[
#                 {"role": "user", "content": f"Summarize this conversation in short bullet points:\n{chat_prompt}"}
#             ]
#         )
#         return msg.content[0].text.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#         return "[Summary unavailable]"

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to PaulBot (Claude). Use POST /chat/ to talk."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         if not any(m["role"] == "system" for m in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         total_chars = sum(len(m["content"]) for m in full_history)

#         if total_chars > 12000:
#             try:
#                 summary = await summarize_messages(full_history[:-10])
#             except Exception as summary_error:
#                 summary = "[Summary unavailable due to API issue]"
#                 print("⚠️ Summarization fallback:", summary_error)

#             prompt = f"Summary of previous conversation:\n{summary}\n\nRecent messages:\n"
#             for msg in full_history[-10:]:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
#         else:
#             prompt = ""
#             for msg in full_history:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

#         msg = client_claude.messages.create(
#             model="claude-3-opus-20240229",
#             max_tokens=1000,
#             temperature=1,
#             messages=[{"role": "user", "content": prompt}]
#         )

#         reply = msg.content[0].text.strip()

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", reply)

#         return {
#             "response": reply,
#             "conversation_id": input.conversation_id
#         }

#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)









# GROQ API

# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# import anthropic
# import groq

# # === Load environment ===
# load_dotenv()
# CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === Clients ===
# client_claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY) if CLAUDE_API_KEY else None
# client_groq = groq.Groq(api_key=GROQ_API_KEY)

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             context = f.read()[:max_chars]
#             print("📄 Loaded context (first 200 chars):", context[:200])
#             return context
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# def save_message(conversation_id: str, role: str, content: str):
#     collection.insert_one({
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     })

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         chat_prompt = "".join([f"{m['role'].capitalize()}: {m['content']}\n" for m in messages])
#         if client_claude:
#             msg = client_claude.messages.create(
#                 model="claude-3-opus-20240229",
#                 max_tokens=400,
#                 temperature=0.3,
#                 messages=[
#                     {"role": "user", "content": f"Summarize this conversation in short bullet points:\n{chat_prompt}"}
#                 ]
#             )
#             return msg.content[0].text.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#     return "[Summary unavailable]"

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to PaulBot (Claude/Groq). Use POST /chat/ to talk."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         if not any(m["role"] == "system" for m in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         total_chars = sum(len(m["content"]) for m in full_history)

#         if total_chars > 12000:
#             summary = await summarize_messages(full_history[:-10])
#             prompt = f"Summary of previous conversation:\n{summary}\n\nRecent messages:\n"
#             for msg in full_history[-10:]:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
#         else:
#             prompt = ""
#             for msg in full_history:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

#         # === Try Claude ===
#         reply = None
#         if client_claude:
#             try:
#                 msg = client_claude.messages.create(
#                     model="claude-3-opus-20240229",
#                     max_tokens=1000,
#                     temperature=1,
#                     messages=[{"role": "user", "content": prompt}]
#                 )
#                 reply = msg.content[0].text.strip()
#             except Exception as e:
#                 print("⚠️ Claude failed, switching to Groq. Error:", e)

#         # === Fallback to Groq with correct model ===
#         if not reply:
#             try:
#                 response = client_groq.chat.completions.create(
#                     model="llama3-70b-8192",  # ✅ Updated model name
#                     messages=[{"role": "user", "content": prompt}],
#                     max_tokens=1000,
#                     temperature=1
#                 )
#                 reply = response.choices[0].message.content.strip()
#             except Exception as e:
#                 print("❌ Groq call failed:", e)
#                 raise HTTPException(status_code=500, detail="Both Claude and Groq failed.")

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", reply)

#         return {
#             "response": reply,
#             "conversation_id": input.conversation_id
#         }

#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)







# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# import anthropic
# import groq

# # === Load environment ===
# load_dotenv()
# CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === Clients ===
# client_claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY) if CLAUDE_API_KEY else None
# client_groq = groq.Groq(api_key=GROQ_API_KEY)

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             context = f.read()[:max_chars]
#             print("📄 Loaded context (first 200 chars):", context[:200])
#             return context
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# def save_message(conversation_id: str, role: str, content: str):
#     collection.insert_one({
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     })

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         chat_prompt = "".join([f"{m['role'].capitalize()}: {m['content']}\n" for m in messages])
#         if client_claude:
#             msg = client_claude.messages.create(
#                 model="claude-3-opus-20240229",
#                 max_tokens=200,
#                 temperature=0.3,
#                 messages=[
#                     {"role": "user", "content": f"Summarize this chat into exactly 3 short and simple bullet points. Be concise and user-friendly.\n{chat_prompt}"}
#                 ]
#             )
#             return msg.content[0].text.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#     return "[Summary unavailable]"

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to PaulBot (Claude/Groq). Use POST /chat/ to talk."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         full_history = load_conversation(input.conversation_id)

#         if not any(m["role"] == "system" for m in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         total_chars = sum(len(m["content"]) for m in full_history)

#         prompt_intro = (
#             "You are PaulBot — a helpful assistant for Paul Merchants customers.\n"
#             "Always use very short, clear language.\n"
#             "When explaining, prefer only 2 or 3 bullet points.\n"
#             "Avoid writing long paragraphs unless the user explicitly asks for detailed information.\n"
#             "Make it easy for any customer to quickly understand.\n\n"
#         )

#         if total_chars > 12000:
#             summary = await summarize_messages(full_history[:-10])
#             prompt = prompt_intro + f"Summary of previous conversation:\n{summary}\n\nRecent messages:\n"
#             for msg in full_history[-10:]:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
#         else:
#             prompt = prompt_intro
#             for msg in full_history:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

#         # === Try Claude ===
#         reply = None
#         if client_claude:
#             try:
#                 msg = client_claude.messages.create(
#                     model="claude-3-opus-20240229",
#                     max_tokens=600,
#                     temperature=0.7,
#                     messages=[{"role": "user", "content": prompt}]
#                 )
#                 reply = msg.content[0].text.strip()
#             except Exception as e:
#                 print("⚠️ Claude failed, switching to Groq. Error:", e)

#         # === Fallback to Groq ===
#         if not reply:
#             try:
#                 response = client_groq.chat.completions.create(
#                     model="llama3-70b-8192",
#                     messages=[{"role": "user", "content": prompt}],
#                     max_tokens=600,
#                     temperature=0.7
#                 )
#                 reply = response.choices[0].message.content.strip()
#             except Exception as e:
#                 print("❌ Groq call failed:", e)
#                 raise HTTPException(status_code=500, detail="Both Claude and Groq failed.")

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", reply)

#         return {
#             "response": reply,
#             "conversation_id": input.conversation_id
#         }

#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)








# import os
# import traceback
# from typing import List, Dict
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from datetime import datetime
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# import anthropic
# import groq

# # === Load environment ===
# load_dotenv()
# CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# if not GROQ_API_KEY:
#     raise ValueError("❌ GROQ_API_KEY missing in .env")
# if not MONGO_URI:
#     raise ValueError("❌ MONGODB_URI missing in .env")
# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")
# if not COLLECTION_NAME:
#     raise ValueError("❌ COLLECTION_NAME missing in .env")

# # === Clients ===
# client_claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY) if CLAUDE_API_KEY else None
# client_groq = groq.Groq(api_key=GROQ_API_KEY)

# # === MongoDB Setup ===
# mongo_client = MongoClient(MONGO_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # === Load context ===
# CONTEXT_FILE = "Pml_queries.txt"

# def load_context(filepath: str, max_chars: int = 3000) -> str:
#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             context = f.read()[:max_chars]
#             print("📄 Loaded context (first 200 chars):", context[:200])
#             return context
#     except Exception as e:
#         print(f"⚠️ Failed to load context: {e}")
#         return ""

# context_text = load_context(CONTEXT_FILE)

# # === FastAPI Setup ===
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # === Models ===
# class UserInput(BaseModel):
#     message: str
#     role: str = "user"
#     conversation_id: str

# def save_message(conversation_id: str, role: str, content: str):
#     collection.insert_one({
#         "conversation_id": conversation_id,
#         "role": role,
#         "content": content,
#         "timestamp": datetime.utcnow()
#     })

# def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
#     messages = list(collection.find(
#         {"conversation_id": conversation_id},
#         sort=[("timestamp", 1)]
#     ))
#     return [{"role": m["role"], "content": m["content"]} for m in messages]

# # === Summarization ===
# async def summarize_messages(messages: List[Dict[str, str]]) -> str:
#     try:
#         chat_prompt = "".join([f"{m['role'].capitalize()}: {m['content']}\n" for m in messages])
#         if client_claude:
#             msg = client_claude.messages.create(
#                 model="claude-3-opus-20240229",
#                 max_tokens=200,
#                 temperature=0.3,
#                 messages=[
#                     {"role": "user", "content": f"Summarize this chat into exactly 3 short and simple bullet points. Be concise and user-friendly.\n{chat_prompt}"}
#                 ]
#             )
#             return msg.content[0].text.strip()
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#     return "[Summary unavailable]"

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to PaulBot (Claude/Groq). Use POST /chat/ to talk."}

# @app.post("/chat/")
# async def chat(input: UserInput):
#     try:
#         if input.message.lower().strip() == "others":
#             # Reset conversation ID
#             new_id = str(datetime.utcnow().timestamp()).replace('.', '')
#             return {
#                 "response": "Sure! Let's start a new conversation. How can I help you?",
#                 "conversation_id": new_id
#             }

#         full_history = load_conversation(input.conversation_id)

#         if not any(m["role"] == "system" for m in full_history):
#             full_history.insert(0, {
#                 "role": "system",
#                 "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
#             })

#         full_history.append({
#             "role": input.role,
#             "content": input.message
#         })

#         total_chars = sum(len(m["content"]) for m in full_history)

#         prompt_intro = (
#             "You are PaulBot — a helpful assistant for Paul Merchants customers.\n"
#             "Always use very short, clear language.\n"
#             "When explaining, prefer only 2 or 3 bullet points.\n"
#             "Avoid writing long paragraphs unless the user explicitly asks for detailed information.\n"
#             "Make it easy for any customer to quickly understand.\n\n"
#         )

#         if total_chars > 12000:
#             summary = await summarize_messages(full_history[:-10])
#             prompt = prompt_intro + f"Summary of previous conversation:\n{summary}\n\nRecent messages:\n"
#             for msg in full_history[-10:]:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
#         else:
#             prompt = prompt_intro
#             for msg in full_history:
#                 prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

#         # === Try Claude ===
#         reply = None
#         if client_claude:
#             try:
#                 msg = client_claude.messages.create(
#                     model="claude-3-opus-20240229",
#                     max_tokens=600,
#                     temperature=0.7,
#                     messages=[{"role": "user", "content": prompt}]
#                 )
#                 reply = msg.content[0].text.strip()
#             except Exception as e:
#                 print("⚠️ Claude failed, switching to Groq. Error:", e)

#         # === Fallback to Groq ===
#         if not reply:
#             try:
#                 response = client_groq.chat.completions.create(
#                     model="llama3-70b-8192",
#                     messages=[{"role": "user", "content": prompt}],
#                     max_tokens=600,
#                     temperature=0.7
#                 )
#                 reply = response.choices[0].message.content.strip()
#             except Exception as e:
#                 print("❌ Groq call failed:", e)
#                 raise HTTPException(status_code=500, detail="Both Claude and Groq failed.")

#         save_message(input.conversation_id, input.role, input.message)
#         save_message(input.conversation_id, "assistant", reply)

#         return {
#             "response": reply,
#             "conversation_id": input.conversation_id
#         }

#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)







import os
import traceback
from typing import List, Dict
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import anthropic
import groq

# === Load environment ===
load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY missing in .env")
if not MONGO_URI:
    raise ValueError("❌ MONGODB_URI missing in .env")
if not DB_NAME:
    raise ValueError("❌ DB_NAME missing in .env")
if not COLLECTION_NAME:
    raise ValueError("❌ COLLECTION_NAME missing in .env")

# === Clients ===
client_claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY) if CLAUDE_API_KEY else None
client_groq = groq.Groq(api_key=GROQ_API_KEY)

# === MongoDB Setup ===
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

# === Load context ===
CONTEXT_FILE = "Pml_queries.txt"

def load_context(filepath: str, max_chars: int = 3000) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            context = f.read()[:max_chars]
            print("📄 Loaded context (first 200 chars):", context[:200])
            return context
    except Exception as e:
        print(f"⚠️ Failed to load context: {e}")
        return ""

context_text = load_context(CONTEXT_FILE)

# === FastAPI Setup ===
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Models ===
class UserInput(BaseModel):
    message: str
    role: str = "user"
    conversation_id: str

def save_message(conversation_id: str, role: str, content: str):
    collection.insert_one({
        "conversation_id": conversation_id,
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow()
    })

def load_conversation(conversation_id: str) -> List[Dict[str, str]]:
    messages = list(collection.find(
        {"conversation_id": conversation_id},
        sort=[("timestamp", 1)]
    ))
    return [{"role": m["role"], "content": m["content"]} for m in messages]

# === Summarization ===
async def summarize_messages(messages: List[Dict[str, str]]) -> str:
    try:
        chat_prompt = "".join([f"{m['role'].capitalize()}: {m['content']}\n" for m in messages])
        if client_claude:
            msg = client_claude.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=200,
                temperature=0.3,
                messages=[
                    {"role": "user", "content": f"Summarize this chat into exactly 3 short and simple bullet points. Be concise and user-friendly.\n{chat_prompt}"}
                ]
            )
            return msg.content[0].text.strip()
    except Exception as e:
        print(f"⚠️ Summarization failed: {e}")
    return "[Summary unavailable]"

@app.get("/")
def read_root():
    return {"message": "Welcome to PaulBot (Claude/Groq). Use POST /chat/ to talk."}

@app.post("/chat/")
async def chat(input: UserInput):
    try:
        if input.message.lower().strip() == "others":
            # Reset conversation ID
            new_id = str(datetime.utcnow().timestamp()).replace('.', '')
            return {
                "response": "Sure! How can I help you 😎?",
                "conversation_id": new_id
            }

        full_history = load_conversation(input.conversation_id)

        if not any(m["role"] == "system" for m in full_history):
            full_history.insert(0, {
                "role": "system",
                "content": f"You are PaulBot — a helpful assistant. Use this context:\n\n{context_text}"
            })

        full_history.append({
            "role": input.role,
            "content": input.message
        })

        total_chars = sum(len(m["content"]) for m in full_history)

        prompt_intro = (
            "You are PaulBot — a helpful assistant for Paul Merchants customers.\n"
            "Always use very short, clear language.\n"
            "When explaining, prefer only 2 or 3 bullet points.\n"
            "Avoid writing long paragraphs unless the user explicitly asks for detailed information.\n"
            "Make it easy for any customer to quickly understand.\n\n"
        )

        if total_chars > 12000:
            summary = await summarize_messages(full_history[:-10])
            prompt = prompt_intro + f"Summary of previous conversation:\n{summary}\n\nRecent messages:\n"
            for msg in full_history[-10:]:
                prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
        else:
            prompt = prompt_intro
            for msg in full_history:
                prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

        # === Try Claude ===
        reply = None
        if client_claude:
            try:
                msg = client_claude.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=600,
                    temperature=0.7,
                    messages=[{"role": "user", "content": prompt}]
                )
                reply = msg.content[0].text.strip()
            except Exception as e:
                print("⚠️ Claude failed, switching to Groq. Error:", e)

        # === Fallback to Groq ===
        if not reply:
            try:
                response = client_groq.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=600,
                    temperature=0.7
                )
                reply = response.choices[0].message.content.strip()
            except Exception as e:
                print("❌ Groq call failed:", e)
                raise HTTPException(status_code=500, detail="Both Claude and Groq failed.")

        save_message(input.conversation_id, input.role, input.message)
        save_message(input.conversation_id, "assistant", reply)

        return {
            "response": reply,
            "conversation_id": input.conversation_id
        }

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Unhandled server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
