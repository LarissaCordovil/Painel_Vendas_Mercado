import pandas as pd
from database.conexao import conectar_banco


def consultar_indicadores_cupons(data_inicio, data_fim):
    con = conectar_banco()
    
    query = f"""
    SELECT
        CAST(ddat_ped AS DATE) AS data_pedido,
        COUNT(CASE WHEN cped_canc = 'N' THEN 1 END) AS cupons_validos, 
        COUNT(CASE WHEN cped_canc = 'S' THEN 1 END) AS cupons_cancelados
    FROM cab_ped
    WHERE 
        CAST(tdthr_ped AS DATE) BETWEEN '{data_inicio}' AND '{data_fim}'
        AND vnum_impfis LIKE 'NFCE_%'
    GROUP BY CAST(ddat_ped AS DATE)
    ORDER BY data_pedido
    """

    df = pd.read_sql(query, con)
    con.close()

    df['data_pedido'] = pd.to_datetime(df['data_pedido'])
    return df