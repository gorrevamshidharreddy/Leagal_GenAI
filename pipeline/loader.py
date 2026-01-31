import pdfplumber
from docx import Document


def extract_text(file):
    file_type = file.name.split(".")[-1].lower()

    if file_type == "pdf":
        return extract_pdf(file)

    elif file_type in ["doc", "docx"]:
        return extract_docx(file)

    elif file_type == "txt":
        return file.read().decode("utf-8")

    else:
        return None


def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
