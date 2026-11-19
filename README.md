# 🏛️ Government Scheme Finder

**Problem Statement:** Citizens don't know which government schemes apply to them.

**Solution:** Upload scheme PDFs → fill a short eligibility form (age, income, state, occupation, category) → the app uses RAG (Retrieval-Augmented Generation) to find and explain matching schemes with specific eligibility reasons.

🔗 **GitHub Repository:** [github.com/PanthDhoriyani/Government-Scheme-Finder](https://github.com/PanthDhoriyani/Government-Scheme-Finder)

---

## How It Works

1. Upload scheme PDFs → text is extracted, chunked, and stored in a FAISS vector store
2. Fill in your profile (age, income, state, occupation, category, gender)
3. Relevant chunks are retrieved via semantic similarity search
4. Gemini LLM reads the chunks and your profile → lists matching schemes with eligibility reasons

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| PDF Parsing | pdfplumber |
| Text Chunking | LangChain RecursiveCharacterTextSplitter |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Store | FAISS (local) |
| LLM | Gemini 3.8 Flash API |

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/PanthDhoriyani/Government-Scheme-Finder.git
cd Government-Scheme-Finder

# 2. Create and activate a virtual environment
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key
# Create a .env file and add:
# GEMINI_API_KEY=your_key_here
# Get a free key at https://aistudio.google.com

# 5. (Optional) Generate sample scheme PDFs for testing
python generate_sample_pdfs.py

# 6. Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## Project Structure

```
Government-Scheme-Finder/
├── app.py                     # Streamlit UI
├── rag_pipeline.py            # PDF ingestion + FAISS indexing
├── llm_query.py               # Prompt builder + Gemini API call
├── generate_sample_pdfs.py    # Script to create test PDFs
├── sample_schemes/            # Sample PDFs for testing
│   ├── pm_kisan.pdf
│   ├── ayushman_bharat.pdf
│   ├── pmay.pdf
│   ├── post_matric_scholarship.pdf
│   └── pm_mudra_yojana.pdf
├── requirements.txt
├── .gitignore                 # Excludes .env and venv/
└── README.md
```

---

## Get a Free Gemini API Key

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API Key** → **Create API key**
3. Create a `.env` file in the project root and paste: `GEMINI_API_KEY=your_key_here`

---

*Built as part of LLM Mini Project Assignment*
