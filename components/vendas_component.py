import streamlit as st
import altair as alt
import pandas as pd
import io
from consultas.consultas import consultar_total_vendas

def painel_vendas(data_inicio, data_fim):
    df_vendas = consultar_total_vendas(data_inicio, data_fim)

    total_vendas = df_vendas['total_vendido'].sum()

    st.subheader("💰 Indicadores de Vendas")
    st.metric("Total Vendido", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    chart = alt.Chart(df_vendas).mark_bar().encode(
        x=alt.X("data_abertura:T", title="Data"),
        y=alt.Y("total_vendido:Q", title="Valor Vendido"),
        tooltip=["data_abertura:T", "total_vendido:Q"]
    ).properties(
        width=700,
        height=300
    )
    st.altair_chart(chart, use_container_width=True)

    # Gerar Excel em memória para download
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_vendas.to_excel(writer, index=False, sheet_name='Vendas')
    processed_data = output.getvalue()

    # Formatar as datas para o nome do arquivo
    data_inicio_str = data_inicio.strftime("%d_%m_%Y")
    data_fim_str = data_fim.strftime("%d_%m_%Y")
    file_name = f"vendas_{data_inicio_str}_a_{data_fim_str}.xlsx"

    st.download_button(
        label="⬇️ Baixar vendas (Excel)",
        data=processed_data,
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )