import streamlit as st
from datetime import datetime, timedelta
from components.vendas_component import painel_vendas

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

#Renderização
painel_vendas(data_inicio, data_fim)