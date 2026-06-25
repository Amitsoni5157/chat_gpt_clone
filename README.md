# My ChatGPT Clone 💬

A simple, interactive ChatGPT Clone built using LangChain, Streamlit, and Multi-LLM Support (Groq & OpenAI). This project focuses on managing Chat History (Memory) and optimizing token usage/costs efficiently.

## ✨ Features
- **Real-time Chat Interface**: Clean, WhatsApp/ChatGPT-like UI built using Streamlit and `streamlit-chat`.
- **Multi-LLM Provider Support**: Fully flexible codebase that allows switching seamlessly between **Groq (Llama 3.1)** and **OpenAI (GPT-4o-mini)** without changing the core logic.
- **Smart Conversation Memory**: Uses `st.session_state` to retain past context and chat history across user interactions.
- **Token Optimization**: Implements context windows by sending only the last 10 messages (`MAX_MESSAGES = 10`) to the LLM, keeping API costs low and responses fast.

## 🛠️ Tech Stack
- **Language**: Python
- **Framework**: Streamlit
- **LLM Orchestration**: LangChain Core
- **LLM Providers**: OpenAI (GPT-4o-mini) / Groq Cloud (Llama 3.1)

## 🚀 Setup Instructions

git clone <your-repo-url>
cd chat_gpt_clone

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

pip install streamlit streamlit-chat langchain-openai langchain-groq langchain-core python-dotenv

# If using OpenAI:
OPENAI_API_KEY=your_openai_api_key_here

# If using Groq:
GROQ_API_KEY=your_groq_api_key_here

streamlit run main.py

Project Structure 

chat_gpt_clone/
│
├── venv/                 # Virtual Environment
├── .env                  # Secret API Keys (Excluded from Git)
├── .gitignore            # Prevents committing venv and .env files
├── main.py               # Main Application Code (Integrated with OpenAI / Groq)
└── README.md             # Project Documentation