import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


EMBED_MODEL = "all-MiniLM-L6-v2"


def extract_text_from_pdfs(uploaded_files) -> str:
    """Extract raw text from a list of uploaded PDF file objects."""
    all_text = ""
    for f in uploaded_files:
        try:
            with pdfplumber.open(f) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        all_text += text + "\n"
        except Exception as e:
            print(f"[WARNING] Could not read {f.name}: {e}")
    return all_text


def build_vectorstore(text: str) -> FAISS:
    """Chunk text and build a FAISS vector store."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=60,
        separators=["\n\n", "\n", ".", " "],
    )
    docs = splitter.create_documents([text])

    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectorstore = FAISS.from_documents(docs, embedder)
    return vectorstore


def load_and_index_pdfs(uploaded_files) -> FAISS:
    """Full pipeline: extract → chunk → embed → index."""
    text = extract_text_from_pdfs(uploaded_files)
    if not text.strip():
        raise ValueError("No text could be extracted from the uploaded PDFs.")
    return build_vectorstore(text)


def retrieve_relevant_chunks(vectorstore: FAISS, query: str, k: int = 6) -> list[str]:
    """Retrieve top-k relevant text chunks for a user query."""
    docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]
