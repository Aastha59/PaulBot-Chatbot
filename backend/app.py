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








import os
from typing import List, Dict
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

# === Load environment variables ===
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

# === Load knowledge context from text file ===
CONTEXT_FILE = "Pml_queries.txt"

def load_context(filepath: str, max_chars: int = 3000) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()[:max_chars]
    except Exception as e:
        print(f"⚠️ Failed to load context: {e}")
        return ""

context_text = load_context(CONTEXT_FILE)

# === Initialize FastAPI ===
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Groq client ===
client = Groq(api_key=GROQ_API_KEY)

# === Request model ===
class UserInput(BaseModel):
    message: str
    role: str = "user"
    conversation_id: str

# === Conversation memory ===
class Conversation:
    def __init__(self):
        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": f"You are a helpful assistant. Use the following knowledge about Paul Merchants while replying:\n\n{context_text}"
            }
        ]
        self.active: bool = True

conversations: Dict[str, Conversation] = {}

def get_or_create_conversation(conversation_id: str) -> Conversation:
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]

def query_groq_api(conversation: Conversation, stream: bool = False) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation.messages,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=stream,
            stop=None,
        )

        if stream:
            response = ""
            for chunk in completion:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    response += delta.content
            if not response.strip():
                raise HTTPException(status_code=500, detail="No content received.")
            return response
        else:
            return completion.choices[0].message.content.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API Error: {str(e)}")

# === Routes ===
@app.get("/")
def read_root():
    return {"message": "Welcome to the ChatBot API. Use POST /chat/ to chat."}

@app.post("/chat/")
async def chat(input: UserInput):
    conversation = get_or_create_conversation(input.conversation_id)

    if not conversation.active:
        raise HTTPException(status_code=400, detail="Session has ended. Please start a new one.")

    try:
        conversation.messages.append({
            "role": input.role,
            "content": input.message
        })

        response = query_groq_api(conversation, stream=False)

        conversation.messages.append({
            "role": "assistant",
            "content": response
        })

        return {
            "response": response,
            "conversation_id": input.conversation_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# === Run if executed directly ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
