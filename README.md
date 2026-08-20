# X Post Generator

An AI-powered **X (formerly Twitter) Post Generator** built with Python, Streamlit, LangChain, and Groq. The application helps users generate engaging, structured, and context-aware social media posts using large language models.

## 🚀 Overview

**X Post Generator** is a simple AI-assisted content generation application designed to streamline the process of creating posts for X.

Instead of manually drafting every post, users can provide a topic, idea, or prompt and generate a polished post through an easy-to-use Streamlit interface.

The project combines **prompt engineering, text preprocessing, and Large Language Models (LLMs)** to generate relevant social media content.

## ✨ Features

* 🤖 **AI-powered post generation**
* ✍️ Generate posts from user-provided topics and prompts
* 🧹 Text preprocessing for cleaner input
* 🧠 LLM-based content generation using Groq
* 🎨 Simple and interactive Streamlit interface
* ⚡ Fast response generation
* 🔐 API credentials managed through environment variables
* 🧩 Modular Python project structure

## 🛠️ Tech Stack

| Technology        | Purpose                                   |
| ----------------- | ----------------------------------------- |
| **Python**        | Core programming language                 |
| **Streamlit**     | Web application interface                 |
| **LangChain**     | LLM integration and application framework |
| **Groq**          | LLM inference                             |
| **Llama 3.3**     | Language model                            |
| **python-dotenv** | Environment variable management           |

## 📁 Project Structure

```text
X-Post-Generator/
│
├── main.py                 # Streamlit application entry point
├── llm_helper.py           # LLM configuration and interaction
├── post_generator.py       # Post generation logic
├── prompt_based.py         # Prompt-based generation functionality
├── preprocessor.py         # Input/text preprocessing
│
├── processed_post.json     # Processed post data
├── raw_post.json           # Raw post data
├── test.py                 # Testing utilities
│
├── .gitignore              # Files excluded from Git
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/hargunnk/X-Post-Generator.git
cd X-Post-Generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key
```

> **Important:** Never commit your `.env` file or expose your API key publicly. The `.gitignore` file is configured to prevent `.env` from being uploaded to GitHub.

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run main.py
```

The application will start locally and provide a URL that can be opened in your browser.

## 🔄 Application Workflow

```text
User Input
    ↓
Text Preprocessing
    ↓
Prompt Generation
    ↓
Groq LLM
    ↓
AI-Generated X Post
    ↓
Streamlit Interface
```

## 🎯 Use Cases

* Creating social media content quickly
* Generating ideas for X posts
* Experimenting with prompt engineering
* Learning LLM application development
* Building AI-powered content creation tools
* Demonstrating Python and Generative AI skills

## 🔐 Security

API credentials are stored using environment variables rather than hard-coded in the source code.

The repository excludes sensitive files such as:

```text
.env
__pycache__/
*.pyc
```

## 🚧 Future Improvements

* Add multiple post-generation styles
* Add tone selection such as professional, humorous, or educational
* Add hashtag and keyword suggestions
* Add post length controls
* Add post history and export functionality
* Add support for additional LLM providers
* Deploy the application using Streamlit Community Cloud

## 📌 Learning Outcomes

This project demonstrates practical experience with:

* Python application development
* Streamlit
* Generative AI
* Large Language Models
* LangChain
* Prompt engineering
* API integration
* Environment variable management
* Git and GitHub

## 👩‍💻 Author

**Hargunn Kaur**

GitHub: [@hargunnk](https://github.com/hargunnk)

