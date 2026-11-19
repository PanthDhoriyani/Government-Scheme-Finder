"""
generate_sample_pdfs.py
Run this ONCE to create sample scheme PDFs for testing.
Requires: pip install fpdf2
"""

from fpdf import FPDF

SCHEMES = [
    {
        "filename": "pm_kisan.pdf",
        "title": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "content": """
PM-KISAN SCHEME DETAILS

Scheme Name: Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)
Ministry: Ministry of Agriculture and Farmers Welfare
Launched: February 2019

ELIGIBILITY CRITERIA:
- The applicant must be a farmer or agricultural labourer.
- The applicant must own cultivable land.
- Annual household income must be below Rs 2,00,000 (2 Lakh rupees).
- All categories (General, OBC, SC, ST) of farmers are eligible.
- Applicable across all states and Union Territories of India.
- Age: No specific age restriction; adult farmers qualify.

BENEFITS:
- Financial assistance of Rs 6,000 per year paid in three equal instalments of Rs 2,000 each.
- Amount is directly credited to the bank account of the beneficiary via DBT.

HOW TO APPLY:
- Visit the official PM-KISAN portal: pmkisan.gov.in
- Register through the local agriculture department or Common Service Centre (CSC).
- Submit Aadhaar card, land records, and bank account details.
- State governments verify and upload eligible farmer data.

EXCLUSIONS:
- Institutional land holders are not eligible.
- Farmers who are or have been holding constitutional posts are excluded.
- Current or former holders of ministerial positions are excluded.
- Income tax payers are not eligible.
""",
    },
    {
        "filename": "ayushman_bharat.pdf",
        "title": "Ayushman Bharat - PM Jan Arogya Yojana (AB-PMJAY)",
        "content": """
AYUSHMAN BHARAT - PM JAN AROGYA YOJANA

Scheme Name: Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (AB-PMJAY)
Ministry: Ministry of Health and Family Welfare
Launched: September 2018

ELIGIBILITY CRITERIA:
- Families listed in the Socio-Economic Caste Census (SECC) 2011 database are eligible.
- Annual household income must be below Rs 1,00,000 (1 Lakh rupees) for urban families.
- Rural families with no permanent house, deprived families, SC/ST households are eligible.
- Applicable across all states that have adopted the scheme.
- Daily wage workers, manual scavengers, domestic workers are eligible.
- Unemployed persons from BPL (Below Poverty Line) households qualify.
- Age: All family members including senior citizens are covered.
- Women-headed households are given priority.

BENEFITS:
- Health coverage of up to Rs 5,00,000 per family per year.
- Covers secondary and tertiary hospitalization.
- Cashless and paperless treatment at empanelled hospitals.
- Pre-existing diseases are covered from day one.

HOW TO APPLY:
- Visit the nearest empanelled hospital or Ayushman Bharat Kendras.
- Check eligibility on mera.pmjay.gov.in or call helpline 14555.
- Present Aadhaar card or ration card for verification.
- No registration fee required.

EXCLUSIONS:
- Families with income above Rs 2.5 Lakh per annum are not eligible.
- Government employees are excluded.
- People with existing health insurance are not eligible.
""",
    },
    {
        "filename": "pmay.pdf",
        "title": "Pradhan Mantri Awas Yojana (PMAY)",
        "content": """
PRADHAN MANTRI AWAS YOJANA (PMAY)

Scheme Name: Pradhan Mantri Awas Yojana - Urban and Rural
Ministry: Ministry of Housing and Urban Affairs
Launched: June 2015

ELIGIBILITY CRITERIA:
- Economically Weaker Section (EWS): Annual household income up to Rs 3,00,000.
- Low Income Group (LIG): Annual household income between Rs 3,00,001 and Rs 6,00,000.
- Middle Income Group I (MIG-I): Annual household income between Rs 6,00,001 and Rs 12,00,000.
- Middle Income Group II (MIG-II): Annual household income between Rs 12,00,001 and Rs 18,00,000.
- The beneficiary family must not own a pucca house anywhere in India.
- Applicable to all categories: General, OBC, SC, ST, EWS.
- Women applicants from EWS and LIG categories are given priority.
- Farmers with low income in rural areas qualify under PMAY-Gramin.
- Senior citizens above 60 years are given ground floor preference.
- Age: 18 years and above.

BENEFITS:
- Interest subsidy of 6.5% for EWS/LIG on home loans up to Rs 6 Lakh for 20 years.
- Interest subsidy of 4% for MIG-I on home loans up to Rs 9 Lakh.
- Interest subsidy of 3% for MIG-II on home loans up to Rs 12 Lakh.
- Financial assistance of Rs 1.2 Lakh to Rs 2.5 Lakh for rural housing construction.

HOW TO APPLY:
- Urban: Apply online at pmaymis.gov.in or visit the local Urban Local Body (ULB).
- Rural: Apply through gram panchayat or AwaasSoft portal.
- Required documents: Aadhaar card, income certificate, land ownership documents, bank account.

EXCLUSIONS:
- Families who already own a pucca house anywhere in India are not eligible.
- Families with income above Rs 18 Lakh per annum are not eligible.
""",
    },
    {
        "filename": "post_matric_scholarship.pdf",
        "title": "Post Matric Scholarship for SC/ST Students",
        "content": """
POST MATRIC SCHOLARSHIP SCHEME FOR SC/ST STUDENTS

Scheme Name: Post Matric Scholarship for Scheduled Caste and Scheduled Tribe Students
Ministry: Ministry of Social Justice and Empowerment / Ministry of Tribal Affairs
Type: Education Scholarship

ELIGIBILITY CRITERIA:
- The applicant must be a student studying at post-matriculation level (Class 11 and above).
- The applicant must belong to Scheduled Caste (SC) or Scheduled Tribe (ST) category.
- Parental or guardian annual income must not exceed Rs 2,50,000 (2.5 Lakh rupees).
- The applicant must be pursuing studies in a government or recognized private institution.
- Age: Typically 16 years to 35 years for most courses.
- Applicable in all states and Union Territories.
- Students enrolled in degree, diploma, certificate, or vocational courses qualify.
- Unemployed SC/ST youth pursuing skill development courses are also eligible.

BENEFITS:
- Full tuition fee reimbursement for government institutions.
- Maintenance allowance ranging from Rs 300 to Rs 1,200 per month depending on course level.
- Book allowance and study tour charges covered.
- Research scholars receive additional allowances.
- Day scholars receive lower maintenance allowance than hostel students.

HOW TO APPLY:
- Apply online at scholarships.gov.in (National Scholarship Portal).
- State-specific portals may also be available.
- Required documents: Caste certificate, income certificate, marksheets, Aadhaar, bank account.
- Application opens annually; check the portal for deadlines.

EXCLUSIONS:
- Students whose parents/guardians have an annual income above Rs 2.5 Lakh are not eligible.
- Students already receiving any other scholarship for the same course.
- Students studying in institutions not recognized by the government.
""",
    },
    {
        "filename": "pm_mudra_yojana.pdf",
        "title": "Pradhan Mantri MUDRA Yojana (PMMY)",
        "content": """
PRADHAN MANTRI MUDRA YOJANA (PMMY)

Scheme Name: Pradhan Mantri Micro Units Development and Refinance Agency (MUDRA) Yojana
Ministry: Ministry of Finance
Launched: April 2015

ELIGIBILITY CRITERIA:
- Self-employed individuals running or planning to start a small or micro business.
- Small business owners, traders, vendors, artisans, and micro entrepreneurs are eligible.
- Farmers who need funds for allied agricultural activities (non-crop) can apply.
- Women entrepreneurs are given priority and preferential interest rates.
- Annual household income: No strict income ceiling, but targeted at low and middle income.
- All categories (General, OBC, SC, ST, EWS) are eligible.
- Age: 18 years to 65 years.
- Applicable across all states and Union Territories.
- Daily wage workers wanting to start self-employment ventures can apply.

LOAN CATEGORIES:
- Shishu: Loans up to Rs 50,000 for startup or very small businesses.
- Kishor: Loans from Rs 50,001 to Rs 5,00,000 for established businesses needing growth capital.
- Tarun: Loans from Rs 5,00,001 to Rs 10,00,000 for larger micro enterprises.
- Tarun Plus: Loans up to Rs 20,00,000 for businesses with good repayment history.

HOW TO APPLY:
- Visit any public sector bank, private bank, microfinance institution, or NBFC.
- Apply online at mudra.org.in or through the respective bank's portal.
- Required documents: Business plan or project report, Aadhaar, PAN card, address proof, bank statements.
- No collateral required for Shishu and Kishor category loans.

EXCLUSIONS:
- Corporate or large enterprises are not eligible.
- Loans for farming or crop cultivation activities (covered under other schemes).
- Applicants with bad credit history may be rejected by the lending institution.
""",
    },
]


def create_pdf(filename, title, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.multi_cell(0, 10, title)
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 7, content.strip())
    pdf.output(f"sample_schemes/{filename}")
    print(f"  Created: sample_schemes/{filename}")


if __name__ == "__main__":
    import os
    os.makedirs("sample_schemes", exist_ok=True)
    print("Generating sample scheme PDFs...")
    for scheme in SCHEMES:
        create_pdf(scheme["filename"], scheme["title"], scheme["content"])
    print("Done! All PDFs saved in sample_schemes/")
