import pandas as pd

def gerar_insights(df):

    insights = {}

    insights["total_linhas"] = df.shape[0]
    insights["total_colunas"] = df.shape[1]

    colunas_numericas = df.select_dtypes(include="number").columns

    if len(colunas_numericas) > 0:

        coluna = colunas_numericas[0]

        insights["coluna_analisada"] = coluna
        insights["media"] = df[coluna].mean()
        insights["maior_valor"] = df[coluna].max()
        insights["menor_valor"] = df[coluna].min()

    return insights