from fpdf import FPDF


name = input("Name: ")
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_margin(0)
pdf.set_font("Times", size=12)
pdf.cell(40, 10, "CS50 Shirtificate")
pdf.image("shirtificate.png", h=pdf.eph, w=pdf.epw/2, x=pdf.epw/2)
pdf.cell(40, 10, f"{name} took CS50")
pdf.output("shirtificate.pdf")
