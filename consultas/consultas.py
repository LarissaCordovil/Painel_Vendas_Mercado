import pandas as pd
from database.conexao import conectar_banco

def consultar_total_vendas(data_inicio, data_fim):
    con = conectar_banco()

    query = f"""
    SELECT 
        CAST(ddt_abre as date), 
        SUM(ntot_vendas)
    FROM ctl_cx
    WHERE ddt_abre BETWEEN '{data_inicio}' AND '{data_fim}'
    GROUP BY CAST(ddt_abre AS DATE)
    ORDER BY CAST(ddt_abre AS DATE)
    """

    df = pd.read_sql(query, con)
    con.close()

    df.columns = ['data_abertura', 'total_vendido']
    df['data_abertura'] = pd.to_datetime(df['data_abertura'])

    return df