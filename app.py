import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import io
import altair as alt
from database.conexao import conectar_banco
from consultas.consultas import consultar_total_vendas

# Título do painel
st.title("Painel de Vendas - Mercado")

#datas padrão: ontem e hoje
hoje = datetime.today().date()
ontem = hoje - timedelta(days=1)

# Datas selecionáveis
data_inicio = st.sidebar.date_input("Data Inicial", value=ontem, format="DD/MM/YYYY")
data_fim = st.sidebar.date_input("Data Final", value=hoje, format="DD/MM/YYYY")

if data_fim < data_inicio:
    st.error("❌ A data final deve ser igual ou posterior à data inicial.")
    st.stop()

#Conectando ao banco
con = conectar_banco()

#Consultar dados 
df = consultar_total_vendas(data_inicio, data_fim)

con.close()

#Formatando os valores 
df['total_vendido_formatado'] = df['total_vendido'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "v").replace(".", ",").replace("v", "."))
df['data_formatada'] = df['data_abertura'].dt.strftime('%d/%m/%Y')

# Exibe dados
st.subheader("Tabela de Vendas")
st.dataframe(df[['data_formatada', 'total_vendido_formatado']].rename(columns={
    'data_formatada': 'Data',
    'total_vendido_formatado': 'Total Vendido'
}))

# Gráfico com Altair
st.subheader("Gráfico de Vendas")
chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('data_formatada:N', title='Data'),
    y=alt.Y('total_vendido:Q', title='Total Vendido'),
    tooltip=[
        alt.Tooltip('data_formatada:N', title='Data'),
        alt.Tooltip('total_vendido:Q', format=',.2f', title='Total R$')
    ]
).properties(
    width=700,
    height=400,
    title='Total Vendido por Dia'
)
st.altair_chart(chart, use_container_width=True)

# Exportar para Excel (arquivo em memória, gerado só quando o usuário clicar)
output = io.BytesIO()
df[['data_abertura', 'total_vendido']].to_excel(output, index=False)
output.seek(0)

st.download_button(
    label="Baixar Excel",
    data=output,
    file_name='total_vendas.xlsx',
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)