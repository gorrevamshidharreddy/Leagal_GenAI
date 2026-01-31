# pipeline/sme_templates.py

SME_TEMPLATES = {
    "Service Agreement": """
This Service Agreement is entered into between the Client and the Service Provider.

1. Scope of Services:
The Service Provider shall perform the services described in Schedule A.

2. Payment:
Payments shall be made within 30 days of invoice.

3. Termination:
Either party may terminate this agreement with 30 days written notice.

4. Confidentiality:
Both parties shall keep all shared information confidential.

5. Governing Law:
This agreement shall be governed by the laws of India.
""",

    "Vendor Agreement": """
This Vendor Agreement governs the supply of goods between the Vendor and Purchaser.

1. Delivery:
Goods shall be delivered within agreed timelines.

2. Pricing:
Prices are fixed and inclusive of applicable taxes.

3. Liability:
Liability is limited to the value of goods supplied.

4. Termination:
Termination allowed with reasonable notice.

5. Jurisdiction:
Courts of India shall have jurisdiction.
"""
}

def get_sme_template(template_name):
    return SME_TEMPLATES.get(template_name, "")
