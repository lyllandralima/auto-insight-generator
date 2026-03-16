import pandas as pd

def carregar_excel(arquivo):

    try:

        df = pd.read_excel(arquivo)

        return df

    except Exception as erro:

        print("Erro ao ler o Excel:", erro)

        return None