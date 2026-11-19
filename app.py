import streamlit as st
from rag_pipeline import load_and_index_pdfs, retrieve_relevant_chunks
from llm_query import find_matching_schemes

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Government Scheme Finder",
    page_icon="🏛️",
    layout="wide",
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏛️ Government Scheme Finder")
st.markdown(
    "Upload government scheme PDFs, fill in your profile, and discover **which schemes you qualify for** — with eligibility reasons."
)
st.divider()

# ── Session state ─────────────────────────────────────────────────────────────
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "indexed_names" not in st.session_state:
    st.session_state.indexed_names = []

# ── Sidebar: PDF Upload ───────────────────────────────────────────────────────
with st.sidebar:
    st.header("📄 Upload Scheme PDFs")
    uploaded_files = st.file_uploader(
        "Upload one or more scheme PDFs",
        type="pdf",
        accept_multiple_files=True,
    )

    if uploaded_files:
        new_names = [f.name for f in uploaded_files]
        if new_names != st.session_state.indexed_names:
            with st.spinner("⏳ Indexing documents…"):
                try:
                    st.session_state.vectorstore = load_and_index_pdfs(uploaded_files)
                    st.session_state.indexed_names = new_names
                    st.success(f"✅ Indexed {len(uploaded_files)} PDF(s)")
                except ValueError as e:
                    st.error(str(e))
        else:
            st.success(f"✅ {len(uploaded_files)} PDF(s) already indexed")

    st.divider()
    st.caption("Built with Streamlit · LangChain · FAISS · Gemini API")

# ── Main: User Profile Form ───────────────────────────────────────────────────
st.subheader("👤 Your Profile")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
    income = st.number_input(
        "Annual Income (₹)",
        min_value=0,
        max_value=10_000_000,
        value=200_000,
        step=10_000,
        format="%d",
    )

with col2:
    state = st.selectbox(
        "State / UT",
        [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
            "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana",
            "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
            "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
            "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
            "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttar Pradesh", "Uttarakhand", "West Bengal",
        ],
    )
    occupation = st.selectbox(
        "Occupation",
        [
            "Farmer / Agricultural Labourer",
            "Student",
            "Unemployed",
            "Salaried Employee",
            "Self-employed / Small Business",
            "Senior Citizen (Retired)",
            "Daily Wage Worker",
            "Woman Entrepreneur",
            "Differently Abled",
        ],
    )

with col3:
    category = st.selectbox("Category", ["General", "OBC", "SC", "ST", "EWS"])
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

st.divider()

# ── Search Button ─────────────────────────────────────────────────────────────
search_clicked = st.button("🔍 Find My Schemes", type="primary", use_container_width=True)

if search_clicked:
    if st.session_state.vectorstore is None:
        st.warning("⚠️ Please upload at least one scheme PDF first.")
    else:
        user_profile = {
            "age": age,
            "income": income,
            "state": state,
            "occupation": occupation,
            "category": category,
            "gender": gender,
        }

        # Build a rich semantic query for retrieval
        query = (
            f"government scheme eligibility for {occupation} aged {age} "
            f"in {state} with annual income {income} rupees "
            f"category {category} gender {gender}"
        )

        with st.spinner("🔎 Searching scheme documents…"):
            chunks = retrieve_relevant_chunks(st.session_state.vectorstore, query, k=6)

        with st.spinner("🤖 Asking the LLM for matching schemes…"):
            try:
                result = find_matching_schemes(user_profile, chunks)
            except Exception as e:
                st.error(f"LLM Error: {e}")
                result = None

        if result:
            st.subheader("✅ Matching Schemes")
            st.markdown(result)

            st.divider()
            with st.expander("📋 Retrieved Context Chunks (for transparency)"):
                for i, chunk in enumerate(chunks, 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.text(chunk)
                    st.markdown("---")
