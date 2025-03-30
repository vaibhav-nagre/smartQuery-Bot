# SmartQuery Bot 🤖

SmartQuery Bot is an intelligent chatbot application built using Streamlit and LangChain. It allows users to interact with a conversational AI that retrieves and processes information from a given website URL. The bot provides detailed and paraphrased responses based on the context of the conversation.

---

## Project Structure
```
SmartQueryBot1/
├── src/
│   ├── app.py          # Main application file
├── .env                # Environment variables (e.g., API keys)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Prerequisites
- Python 3.8 or higher
- [Streamlit](https://streamlit.io/)
- OpenAI API key (for ChatGPT integration)
- ChromaDB setup (for vector storage)

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/SmartQueryBot1.git
   cd SmartQueryBot1
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Run the Application**:
   ```bash
   streamlit run src/app.py
   ```

---

## Usage Instructions

1. Open the application in your browser (Streamlit will provide a local URL).
2. Enter a website URL in the sidebar.
3. Type your query in the chat input box.
4. The bot will process your query and provide a detailed response.

---

## License
This project is licensed under the MIT License.
