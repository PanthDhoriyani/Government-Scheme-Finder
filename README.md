# 🏛️ Government Scheme Finder

**Problem Statement:** Citizens don't know which government schemes apply to them.

**Solution:** Upload scheme PDFs → fill a short eligibility form (age, income, state, occupation, category) → the app uses RAG (Retrieval-Augmented Generation) to find and explain matching schemes with specific eligibility reasons.

---

## How It Works

1. Upload scheme PDFs → text is extracted, chunked, and stored in a FAISS vector store
2. Fill in your profile (age, income, state, occupation, category, gender)
3. Relevant chunks are retrieved via semantic similarity search
4. Gemini LLM reads the chunks and your profile → lists matching schemes with eligibility reasons

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| PDF Parsing | pdfplumber |
| Text Chunking | LangChain RecursiveCharacterTextSplitter |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Store | FAISS (local) |
| LLM | Gemini 2.0 Flash API |

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Gemini API key
# Create a .env file:
echo GEMINI_API_KEY=your_key_here > .env

# 4. (Optional) Generate sample scheme PDFs
python generate_sample_pdfs.py

# 5. Run the app
streamlit run app.py
```

## Project Structure

```
assignment_3/
├── app.py                     # Streamlit UI
├── rag_pipeline.py            # PDF ingestion + FAISS indexing
├── llm_query.py               # Prompt builder + Gemini API call
├── generate_sample_pdfs.py    # Script to create test PDFs
├── sample_schemes/            # Sample PDFs (generated)
├── requirements.txt
├── .gitignore
└── screenshots/
```

## Get a Free Gemini API Key

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API Key** → **Create API key**
3. Paste it in your `.env` file

---

*Built as part of LLM Mini Project Assignment*
