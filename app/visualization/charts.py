import plotly.express as px


def gerar_graficos(df):

    graficos = []

    colunas_numericas = df.select_dtypes(include="number").columns

    if len(colunas_numericas) == 0:
        return graficos

    coluna = colunas_numericas[0]

    # gráfico de distribuição
    fig1 = px.histogram(
        df,
        x=coluna,
        title=f"Distribuição de {coluna}"
    )

    graficos.append(fig1)

    # gráfico de barras com top valores
    top_df = df.sort_values(by=coluna, ascending=False).head(10)

    fig2 = px.bar(
        top_df,
        x=top_df.index,
        y=coluna,
        title=f"Top 10 valores de {coluna}"
    )

    graficos.append(fig2)

    return graficos