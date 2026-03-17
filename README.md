# Auto Insight Generator

Ferramenta de análise automática de planilhas Excel desenvolvida em Python com Streamlit.

## Objetivo
Automatizar a leitura, interpretação e visualização de dados de planilhas, gerando insights e dashboards de forma rápida e intuitiva.

## Funcionalidades
- Upload de arquivos Excel
- Interpretação automática de colunas
- Filtros categóricos, numéricos e por data
- Insights automáticos
- Dashboard interativo
- Geração de relatório em PDF

## Tecnologias utilizadas
- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL
- FPDF

## Estrutura do projeto
- `data`: leitura e tratamento inicial dos arquivos
- `analysis`: interpretação da estrutura da planilha
- `insights`: geração de insights automáticos
- `visualization`: criação de gráficos e dashboards
- `ui`: filtros e componentes da interface
- `reports`: geração de relatório PDF
- `main.py`: ponto de entrada da aplicação

## Como executar
```bash
pip install -r requirements.txt
streamlit run app/main.py