# 3-Agenti Chat Bot

A Streamlit-based AI agent application built with `langgraph`, `langchain`, and multiple LLM connectors. The project supports three use cases: Basic Chatbot, Chatbot with Web (tool integration), and AI News summarization.

## 🚀 Features

- Select between `Groq` and `OpenAI` LLM providers
- Use case options:
  - Basic Chatbot
  - Chatbot with Web
  - AI News
- Streamlit-powered UI for interactive chat
- Support for tool-based search functionality via Tavily
- AI news fetch + markdown summary generation

## 📦 Requirements

- Python 3.14 or later
- `pip` package manager

## 🧩 Dependencies

The project uses these main dependencies:

- `faiss-cpu`
- `langchain`
- `langchain-community`
- `langchain-core`
- `langchain-groq`
- `langchain-openai`
- `langchain-tavily`
- `langgraph`
- `python-dotenv`
- `streamlit`
- `tavily-python`

Dependencies are listed in `pyproject.toml` and `req.txt`.

## 🔧 Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/3-Agenti_chat_bot.git
cd 3-Agenti_chat_bot

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows PowerShell
.venv\Scripts\Activate.ps1
# or Windows CMD
.venv\Scripts\activate

# Install dependencies
pip install -r req.txt
```

> If you prefer, you can also install directly from `pyproject.toml` with `pip install .`.

## ⚙️ Configuration

The app can load API keys from the Streamlit sidebar or from environment variables.

Required keys for each provider:

- `OPENAI_API_KEY` for OpenAI
- `GROQ_API_KEY` for Groq
- `TAVILY_API_KEY` for Tavily (required for Chatbot with Web and AI News)

Create a `.env` file in the repository root for convenience:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## ▶️ Running the App

Run the Streamlit application using either of these commands:

```bash
streamlit run app.py
```

or

```bash
python app.py
```

Then open the browser URL shown by Streamlit.

## 🧪 Usage

1. Start the app.
2. In the sidebar, select your LLM provider (`Groq` or `OpenAi`).
3. Enter the required API key for your selected provider.
4. Choose a use case:
   - `Basic Chatbot`
   - `Chatbot with Web`
   - `AI News`
5. For `Chatbot with Web` and `AI News`, enter `TAVILY_API_KEY` as well.
6. Enter your message in the chat box and submit.

## 📁 Project Structure

```
app.py
main.py
pyproject.toml
README.md
req.txt
src/
  langgrapg_agentic_ai/
    main.py
    graph/
      graph_builder.py
    LLMS/
      groqllm.py
      openai.py
    nodes/
      basic_chatbot_node.py
      chatbot_with_Tool_node.py
      ai_news_node.py
    state/
      state.py
    tools/
      search_tool.py
    ui/
      uiconfigfile.ini
      uiconfigfile.py
      streamlit_ui/
        display_result.py
        loadui.py
```

## 💻 Git Commands

```bash
# Initialize a repo (if needed)
git init

git add .
git commit -m "Initial project setup"

git branch -M main

git remote add origin https://github.com/<your-username>/3-Agenti_chat_bot.git

git push -u origin main
```

## 📝 Notes

- `app.py` launches the Streamlit UI and loads the LangGraph AgenticAI workflow.
- `pyproject.toml` declares package metadata and dependencies.
- `req.txt` is provided for straightforward installation.

## 📌 License

Add your preferred license here.


<img width="1912" height="822" alt="image" src="https://github.com/user-attachments/assets/e158a038-43a9-4650-9777-9b26cf194861" />
