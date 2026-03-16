import plotly.express as px


def gerar_graficos_inteligentes(df):

    graficos = []

    colunas_numericas = df.select_dtypes(include="number").columns
    colunas_texto = df.select_dtypes(include="object").columns

    # Histograma para colunas numéricas
    for coluna in colunas_numericas:

        fig = px.histogram(
            df,
            x=coluna,
            title=f"Distribuição de {coluna}"
        )

        graficos.append(fig)

    # Barras para categoria + valor
    if len(colunas_texto) > 0 and len(colunas_numericas) > 0:

        categoria = colunas_texto[0]
        valor = colunas_numericas[0]

        agrupado = df.groupby(categoria)[valor].sum().reset_index()

        fig = px.bar(
            agrupado,
            x=categoria,
            y=valor,
            title=f"{valor} por {categoria}"
        )

        graficos.append(fig)

    return graficos