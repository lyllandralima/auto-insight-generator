import streamlit as st
from data.loader import carregar_excel
from insights.insight_engine import gerar_insights
from visualization.charts import gerar_graficos
from analysis.column_interpreter import interpretar_colunas
from insights.smart_insights import gerar_insights_inteligentes
from visualization.smart_charts import gerar_graficos_inteligentes
from reports.report_generator import gerar_relatorio

st.title("Auto Insight Generator")

st.write("Envie uma planilha Excel para análise automática")

arquivo = st.file_uploader(
    "Upload do arquivo Excel",
    type=["xlsx"]
)

if arquivo is not None:

    df = carregar_excel(arquivo)

    if df is not None:

        st.subheader("Preview da planilha")

        st.dataframe(df)

        st.write("Linhas:", df.shape[0])
        st.write("Colunas:", df.shape[1])

        st.subheader("Insights automáticos")

        insights = gerar_insights(df)

        for chave, valor in insights.items():
            st.write(f"{chave}: {valor}")
        st.subheader("Visualização dos dados")

        st.subheader("Dashboard automático")

        graficos = gerar_graficos(df)

        for fig in graficos:
            st.plotly_chart(fig)

        st.subheader("Interpretação das colunas")

        interpretacao = interpretar_colunas(df)

        for coluna, tipo in interpretacao.items():
            st.write(f"{coluna} → {tipo}")
        st.subheader("Análise automática")

        analises = gerar_insights_inteligentes(df)

        for frase in analises:
            st.write(frase)

        st.subheader("Dashboard automático")

        graficos = gerar_graficos_inteligentes(df)

        for grafico in graficos:
            st.plotly_chart(grafico)
        if st.button("Gerar Relatório"):
            caminho = gerar_relatorio(analises)

            st.success("Relatório gerado!")