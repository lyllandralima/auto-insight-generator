import streamlit as st
from data.loader import carregar_excel
from insights.insight_engine import gerar_insights
from analysis.column_interpreter import interpretar_colunas
from insights.smart_insights import gerar_insights_inteligentes
from visualization.smart_charts import gerar_graficos_inteligentes
from reports.report_generator import gerar_relatorio
from ui.filters import aplicar_filtros

st.set_page_config(
    page_title="Auto Insight Generator",
    layout="wide"
)

st.title("Auto Insight Generator")
st.markdown("Ferramenta para análise automática de planilhas Excel.")

arquivo = st.file_uploader(
    "Faça upload de uma planilha Excel",
    type=["xlsx"]
)

if arquivo is not None:

    df = carregar_excel(arquivo)

    if df is None:
        st.error("Não foi possível ler a planilha. Verifique se o arquivo está no formato correto.")
    elif df.empty:
        st.warning("A planilha enviada está vazia.")
    else:
        df_filtrado = aplicar_filtros(df)

        if df_filtrado.empty:
            st.warning("Nenhum dado encontrado com os filtros aplicados.")
        else:
            insights = gerar_insights(df_filtrado)
            interpretacao = interpretar_colunas(df_filtrado)
            analises = gerar_insights_inteligentes(df_filtrado)
            graficos = gerar_graficos_inteligentes(df_filtrado)

            st.subheader("Resumo da planilha")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Linhas", df_filtrado.shape[0])

            with col2:
                st.metric("Colunas", df_filtrado.shape[1])

            with col3:
                coluna_analisada = insights.get("coluna_analisada", "N/A")
                st.metric("Coluna principal", coluna_analisada)

            with st.expander("Visualizar dados da planilha"):
                st.dataframe(df_filtrado, use_container_width=True)

            st.subheader("Insights automáticos")

            for chave, valor in insights.items():
                st.write(f"**{chave}**: {valor}")

            st.subheader("Interpretação das colunas")

            for coluna, tipo in interpretacao.items():
                st.write(f"**{coluna}** → {tipo}")

            st.subheader("Análise automática")

            for frase in analises:
                st.write(f"- {frase}")

            st.subheader("Dashboard automático")

            for grafico in graficos:
                st.plotly_chart(grafico, use_container_width=True)

            if st.button("Gerar Relatório"):
                caminho = gerar_relatorio(analises)
                st.success(f"Relatório gerado com sucesso: {caminho}")