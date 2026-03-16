def interpretar_colunas(df):

    interpretacao = {}

    for coluna in df.columns:

        nome = coluna.lower()

        if "cost" in nome or "price" in nome:
            interpretacao[coluna] = "valor"

        elif "qty" in nome or "quant" in nome or "volume" in nome:
            interpretacao[coluna] = "quantidade"

        elif "date" in nome:
            interpretacao[coluna] = "data"

        elif "supplier" in nome or "vendor" in nome:
            interpretacao[coluna] = "fornecedor"

        elif "product" in nome or "part" in nome:
            interpretacao[coluna] = "produto"

        else:
            interpretacao[coluna] = "desconhecido"

    return interpretacao