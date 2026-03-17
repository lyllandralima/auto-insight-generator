from fpdf import FPDF
from datetime import datetime


def gerar_relatorio(dados):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Relatorio Automatico de Analise", ln=True)

    pdf.ln(5)

    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, f"Gerado em: {data_atual}", ln=True)

    pdf.ln(5)

    if isinstance(dados, list):
        for item in dados:
            pdf.multi_cell(0, 10, f"- {str(item)}")
            pdf.ln(1)

    elif isinstance(dados, dict):
        for chave, valor in dados.items():
            texto = f"{chave}: {valor}"
            pdf.multi_cell(0, 10, texto)
            pdf.ln(1)

    nome_arquivo = datetime.now().strftime("relatorio_%Y%m%d_%H%M%S.pdf")
    pdf.output(nome_arquivo)

    return nome_arquivo