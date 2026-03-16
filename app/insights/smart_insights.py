import pandas as pd


def gerar_insights_inteligentes(df):

    textos = []

    colunas_numericas = df.select_dtypes(include="number").columns

    for coluna in colunas_numericas:

        media = df[coluna].mean()
        maximo = df[coluna].max()
        minimo = df[coluna].min()

        textos.append(
            f"A média da coluna {coluna} é {media:.2f}."
        )

        textos.append(
            f"O maior valor encontrado em {coluna} foi {maximo}."
        )

        textos.append(
            f"O menor valor encontrado em {coluna} foi {minimo}."
        )

    return textos
