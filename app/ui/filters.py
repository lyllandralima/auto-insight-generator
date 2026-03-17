import streamlit as st
import pandas as pd


def aplicar_filtros(df):
    df_filtrado = df.copy()

    st.subheader("Filtros")

    # Filtro categórico
    colunas_categoricas = df_filtrado.select_dtypes(include="object").columns.tolist()

    if len(colunas_categoricas) > 0:
        coluna_filtro = st.selectbox(
            "Escolha uma coluna categórica para filtrar",
            options=["Nenhum"] + colunas_categoricas
        )

        if coluna_filtro != "Nenhum":
            valores_disponiveis = sorted(
                df_filtrado[coluna_filtro].dropna().astype(str).unique().tolist()
            )

            valores_selecionados = st.multiselect(
                f"Selecione valores de {coluna_filtro}",
                options=valores_disponiveis
            )

            if valores_selecionados:
                df_filtrado = df_filtrado[
                    df_filtrado[coluna_filtro].astype(str).isin(valores_selecionados)
                ]

    # Filtro numérico
    colunas_numericas = df_filtrado.select_dtypes(include="number").columns.tolist()

    if len(colunas_numericas) > 0:
        coluna_numerica = st.selectbox(
            "Escolha uma coluna numérica para filtrar",
            options=["Nenhum"] + colunas_numericas
        )

        if coluna_numerica != "Nenhum":
            valor_min = float(df_filtrado[coluna_numerica].min())
            valor_max = float(df_filtrado[coluna_numerica].max())

            faixa_valores = st.slider(
                f"Selecione a faixa de valores para {coluna_numerica}",
                min_value=valor_min,
                max_value=valor_max,
                value=(valor_min, valor_max)
            )

            df_filtrado = df_filtrado[
                (df_filtrado[coluna_numerica] >= faixa_valores[0]) &
                (df_filtrado[coluna_numerica] <= faixa_valores[1])
            ]

    # Filtro de data
    colunas_data = []

    for coluna in df_filtrado.columns:
        try:
            coluna_convertida = pd.to_datetime(df_filtrado[coluna], errors="coerce")
            if coluna_convertida.notna().sum() > 0:
                colunas_data.append(coluna)
        except Exception:
            pass

    if len(colunas_data) > 0:
        coluna_data = st.selectbox(
            "Escolha uma coluna de data para filtrar",
            options=["Nenhum"] + colunas_data
        )

        if coluna_data != "Nenhum":
            serie_data = pd.to_datetime(df_filtrado[coluna_data], errors="coerce").dropna()

            if not serie_data.empty:
                data_min = serie_data.min().date()
                data_max = serie_data.max().date()

                intervalo_datas = st.date_input(
                    f"Selecione o período de {coluna_data}",
                    value=(data_min, data_max)
                )

                if len(intervalo_datas) == 2:
                    data_inicio, data_fim = intervalo_datas

                    df_filtrado[coluna_data] = pd.to_datetime(
                        df_filtrado[coluna_data], errors="coerce"
                    )

                    df_filtrado = df_filtrado[
                        (df_filtrado[coluna_data].dt.date >= data_inicio) &
                        (df_filtrado[coluna_data].dt.date <= data_fim)
                    ]

    return df_filtrado