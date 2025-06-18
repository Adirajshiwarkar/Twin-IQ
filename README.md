# Twin-IQ
# 🧠⇄🧠 TwinIQ – Gemini-Powered AI Chatbot

TwinIQ is a smart and lightweight conversational chatbot interface built using **Streamlit** and powered by **Gemini-Pro** via Google's Generative AI API. Designed to be intuitive, responsive, and visually sleek, TwinIQ helps users explore ideas, ask questions, and engage in intelligent conversations.

---

## 🚀 Features

* 🔌 **Integrates Google’s Gemini-Pro (`gemini-1.5-flash-latest`) model**
* 💬 **Real-time chatbot interface using Streamlit**
* 📜 **Maintains conversational history during sessions**
* 🌐 **Environment-secured API key management**
* 🧠 **Minimalist UI with personality-driven prompts**
* 🧪 **Easily extendable with APIs like weather, news, etc.**

---

## 🧱 Tech Stack

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| `Streamlit`           | Frontend chatbot interface |
| `google.generativeai` | Gemini-Pro model access    |
| `dotenv`              | Load environment variables |
| `Python`              | Base language              |

---

## 📁 File Structure

```plaintext
├── app.py               # Main Streamlit application
├── .env                 # Contains Google API key (not committed)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧪 Code Walkthrough

### 🔑 API Key Setup

```python
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
```

* Loads `.env` file securely.
* Configures Google Generative AI client.

---

### 🤖 Initialize Model

```python
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
```

* Uses the latest **Gemini 1.5 Flash** model for fast, lightweight responses.

---

### 💬 Chat Session

```python
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
```

* Ensures chat context is maintained throughout the session.

---

### 🧠 User & Assistant Interface

```python
st.title("🧠⇄🧠 TwinIQ")
user_prompt = st.chat_input("👋 “Hi! I’m TwinIQ, your smart AI assistant —Let’s explore your questions together!”")
```

* Beautiful prompt to engage the user.
* Captures user input and sends it to Gemini.

---

### 📤 Message Exchange

```python
gemini_response = st.session_state.chat_session.send_message(user_prompt)
st.markdown(gemini_response.text)
```

* Sends prompt to Gemini.
* Displays assistant's response in the chat format.

---

## 🔒 Environment Variable Setup

Create a `.env` file in the root directory:

```bash
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

Make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

Then run the app:

```bash
streamlit run app.py
```

---

## 🧠 About the Name “TwinIQ”

**TwinIQ** blends the concept of:

* **"Twin"** – Representing Gemini (twins), and the dual-natured intelligence of human + AI.
* **"IQ"** – Intelligence quotient, smart responses.

> Together: “Your intelligent twin assistant for anything you think or ask.”

---

## 🪪 License

MIT License

---

## 🤝 Contributions

Feel free to fork, extend, or integrate weather/news APIs. PRs are welcome!

---

## 📸 UI Preview

> (Add a screenshot of the interface here if needed)

---

## ✨ Follow-up Ideas

* 🌦️ Integrate weather updates (OpenWeatherMap)
* 🌍 Add multilingual support
* 🧹 Plug in custom plugins for reminders, to-do lists, or content generation

---
