import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def build_prompt(user_profile: dict, context_chunks: list[str]) -> str:
    context = "\n\n---\n\n".join(context_chunks)
    prompt = f"""You are an expert Government Scheme Eligibility Advisor for India.

Your job is to read the SCHEME DOCUMENTS below and identify every scheme the user qualifies for based on their PROFILE.

For each matching scheme, respond with:
1. **Scheme Name**
2. **Eligibility Reason** – quote or paraphrase the exact criteria from the document that this user meets
3. **Benefits** – what the user will receive
4. **How to Apply** – steps or portal (if mentioned in the document)

If the user does not qualify for any scheme found in the documents, say so clearly and explain why.

=== USER PROFILE ===
- Age           : {user_profile['age']} years
- Annual Income : ₹{user_profile['income']:,}
- State         : {user_profile['state']}
- Occupation    : {user_profile['occupation']}
- Category      : {user_profile.get('category', 'General')}
- Gender        : {user_profile.get('gender', 'Not specified')}

=== SCHEME DOCUMENTS ===
{context}

Now list all matching schemes with detailed eligibility reasoning:
"""
    return prompt


def find_matching_schemes(user_profile: dict, context_chunks: list[str]) -> str:
    """Call Gemini API and return the LLM response."""
    prompt = build_prompt(user_profile, context_chunks)
    model = genai.GenerativeModel("gemini-3.8-flash")
    response = model.generate_content(prompt)
    return response.text
