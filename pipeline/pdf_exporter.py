# pipeline/pdf_exporter.py

from fpdf import FPDF

def generate_legal_pdf(summary, clause_results, output_path="legal_review.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    pdf.cell(0, 10, "Contract Legal Review Summary", ln=True)
    pdf.multi_cell(0, 8, summary)

    pdf.ln(5)

    for clause in clause_results:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, clause["clause_id"] + " - " + clause["title"], ln=True)

        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 6, clause["text"])

        pdf.cell(0, 6, f"Risk Level: {clause['risk']}", ln=True)

        if clause["compliance"]:
            pdf.multi_cell(0, 6, "Compliance Flags: " + ", ".join(clause["compliance"]))

        if clause["ambiguity"]["is_ambiguous"]:
            pdf.multi_cell(0, 6, "Ambiguous Terms: " + ", ".join(clause["ambiguity"]["terms"]))

        pdf.ln(3)

    pdf.output(output_path)
    return output_path
