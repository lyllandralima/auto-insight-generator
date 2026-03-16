from fpdf import FPDF


def gerar_relatorio(insights):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatorio Automatico", ln=True)

    for insight in insights:

        pdf.cell(200, 10, txt=insight, ln=True)

    caminho = "relatorio.pdf"

    pdf.output(caminho)

    return caminho