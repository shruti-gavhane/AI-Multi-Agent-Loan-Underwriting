import io
from typing import Dict

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report: Dict):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Header
    title = Paragraph("<b>ABC Finance Ltd.</b>", styles["Title"])
    subtitle = Paragraph("<b>Loan Sanction Letter</b>", styles["Heading2"])

    elements.append(title)
    elements.append(subtitle)
    elements.append(Spacer(1, 20))

    # Greeting
    greeting = Paragraph(
        f"Dear <b>{report['name']}</b>,",
        styles["Normal"]
    )
    elements.append(greeting)
    elements.append(Spacer(1, 12))

    intro = Paragraph(
        f"We are pleased to inform you that your loan application has been "
        f"<b>{report['decision']}</b> after evaluation by our underwriting system.",
        styles["Normal"]
    )
    elements.append(intro)
    elements.append(Spacer(1, 20))

    # Loan details table
    loan_data = [
        ["Field", "Value"],
        ["Applicant Name", report["name"]],
        ["Decision", report["decision"]],
        ["Risk Score", str(report["risk_score"])],
        ["Risk Band", report["risk_band"]],
        ["Interest Rate", f"{report['interest_rate']}%"],
        ["Estimated EMI", f"INR {report['emi']}"],
        ["KYC Status", report["kyc_status"]],
    ]

    table = Table(loan_data, colWidths=[180, 250])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # Underwriting summary
    elements.append(Paragraph("<b>Underwriting Summary</b>", styles["Heading3"]))
    elements.append(Spacer(1, 8))

    explanation_lines = report["explanation"].splitlines()
    for line in explanation_lines:
        elements.append(Paragraph(f"• {line}", styles["Normal"]))

    elements.append(Spacer(1, 20))

    # Terms and Conditions
    elements.append(Paragraph("<b>Terms & Conditions</b>", styles["Heading3"]))
    elements.append(Spacer(1, 8))

    terms = [
        "EMI must be paid before the due date every month.",
        "Late payments may attract penalties.",
        "Defaulting may impact your creditworthiness.",
        "Loan approval is subject to final bank policy verification."
    ]

    for term in terms:
        elements.append(Paragraph(f"• {term}", styles["Normal"]))

    elements.append(Spacer(1, 30))

    # Signature
    elements.append(Paragraph("Authorized By,", styles["Normal"]))
    elements.append(Spacer(1, 25))
    elements.append(Paragraph("<b>Loan Approval Officer</b>", styles["Normal"]))
    elements.append(Paragraph("ABC Finance Ltd.", styles["Normal"]))

    # Build PDF
    doc.build(elements)

    buffer.seek(0)
    return buffer
