import pandas as pd


def gerar_insights_inteligentes(df):

    textos = []

    colunas_numericas = df.select_dtypes(include="number").columns

    if len(colunas_numericas) == 0:
        textos.append("Não foram encontradas colunas numéricas para análise.")
        return textos

    for coluna in colunas_numericas:

        media = df[coluna].mean()
        maximo = df[coluna].max()
        minimo = df[coluna].min()
        desvio = df[coluna].std()

        textos.append(
            f"A coluna {coluna} apresenta média de {media:.2f}."
        )

        textos.append(
            f"O maior valor identificado em {coluna} foi {maximo:.2f}, enquanto o menor foi {minimo:.2f}."
        )

        if pd.notna(desvio):
            textos.append(
                f"A dispersão dos valores de {coluna} indica um desvio padrão de {desvio:.2f}."
            )

    return textos