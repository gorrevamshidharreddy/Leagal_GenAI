import streamlit as st
import os
import json

# Pipeline imports
from pipeline.loader import extract_text
from pipeline.classifier import classify_contract
from pipeline.clause_extractor import extract_clauses
from pipeline.risk_engine import assess_clause_risk
from pipeline.compliance_engine import check_indian_compliance
from pipeline.ambiguity_detector import detect_ambiguity
from pipeline.template_matcher import match_clause_to_template
from pipeline.sme_templates import get_sme_template
from pipeline.pdf_exporter import generate_legal_pdf


# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="Legal GenAI Assistant", layout="wide")
st.title("📜 GenAI Legal Assistant for Indian SMEs")
st.write("Upload a contract to analyze risks, compliance, and clarity in plain language.")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

# ---------------- SME TEMPLATE SECTION ----------------
st.sidebar.header("📄 SME Contract Templates")
template_choice = st.sidebar.selectbox(
    "View SME-Friendly Template",
    ["None", "Service Agreement", "Vendor Agreement"]
)

if template_choice != "None":
    template_text = get_sme_template(template_choice)
    st.sidebar.text_area(
        f"{template_choice} Template",
        template_text,
        height=300
    )

# ---------------- MAIN PIPELINE ----------------
if uploaded_file is not None:
    with st.spinner("Extracting contract text..."):
        contract_text = extract_text(uploaded_file)

    if not contract_text.strip():
        st.error("Could not extract text from the document.")
        st.stop()

    # ---- Contract Classification ----
    with st.spinner("Classifying contract type..."):
        contract_type = classify_contract(contract_text)

    st.success(f"📌 Contract Type Detected: **{contract_type}**")

    # ---- Clause Extraction ----
    clauses = extract_clauses(contract_text)
    st.info(f"🔍 Total Clauses Detected: {len(clauses)}")

    clause_results = []
    risk_score_map = {"Low": 1, "Medium": 2, "High": 3}
    total_risk_score = 0

    st.header("📑 Clause-by-Clause Analysis")

    for clause in clauses:
        clause_text = clause["text"]

        risk = assess_clause_risk(clause_text)
        compliance = check_indian_compliance(clause_text)
        ambiguity = detect_ambiguity(clause_text)
        similarity = match_clause_to_template(clause_text)

        total_risk_score += risk_score_map.get(risk, 1)

        with st.expander(f"{clause['clause_id']} - {clause['title']}"):
            st.write(clause_text)

            st.markdown(f"**Risk Level:** `{risk}`")

            if compliance:
                st.warning("⚖️ Compliance Flags:")
                for c in compliance:
                    st.write(f"- {c}")

            if ambiguity["is_ambiguous"]:
                st.warning("❓ Ambiguous Terms Detected:")
                st.write(", ".join(ambiguity["terms"]))

            if similarity["matched_template"]:
                st.info(
                    f"📘 Similar to **{similarity['matched_template']}** template "
                    f"({similarity['similarity_percent']}% match)"
                )

        clause_results.append({
            "clause_id": clause["clause_id"],
            "title": clause["title"],
            "text": clause_text,
            "risk": risk,
            "compliance": compliance,
            "ambiguity": ambiguity
        })

    # ---- Contract Level Risk ----
    avg_risk = total_risk_score / max(len(clauses), 1)

    if avg_risk < 1.5:
        overall_risk = "Low"
    elif avg_risk < 2.3:
        overall_risk = "Medium"
    else:
        overall_risk = "High"

    st.subheader("📊 Overall Contract Risk")
    st.markdown(f"### 🔴 **{overall_risk} Risk Contract**")

    # ---- PDF Export ----
    st.header("📄 Export for Legal Review")

    if st.button("Generate PDF Report"):
        summary_text = (
            f"Contract Type: {contract_type}\n"
            f"Overall Risk Level: {overall_risk}\n"
            f"Total Clauses Analyzed: {len(clauses)}"
        )

        pdf_path = generate_legal_pdf(
            summary=summary_text,
            clause_results=clause_results
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Legal Review PDF",
                data=f,
                file_name="legal_contract_review.pdf",
                mime="application/pdf"
            )

    # ---- Audit Log (Optional but impressive) ----
    audit_log = {
        "contract_type": contract_type,
        "overall_risk": overall_risk,
        "total_clauses": len(clauses)
    }

    with open("audit_log.json", "w") as log_file:
        json.dump(audit_log, log_file, indent=2)
