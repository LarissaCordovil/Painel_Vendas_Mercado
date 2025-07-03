# 📊 Painel de Vendas - Sistema Dynamis(Em Desenvolvimento)

Projeto de painel interativo criado com **Python** e **Streamlit**, que se conecta a uma base de dados **Firebird** para exibir indicadores de vendas diárias. Desenvolvido com dados reais, utilizado em um mercado.

> 🔗 Repositório: [Painel_Vendas_Mercado](https://github.com/LarissaCordovil/Painel_Vendas_Mercado)

## 🚀 Objetivo

Construir um painel funcional, com visualização clara e exportação dos dados de vendas, como parte do portfólio profissional.

## 🧰 Tecnologias Utilizadas

- Python 3.13  
- Streamlit  
- Pandas  
- Altair  
- OpenPyXL  
- FDB (conector Firebird para Python)  
- python-dotenv  

## 📁 Estrutura do Projeto
Painel_Vendas_Mercado/
│
├── app.py # Interface principal com Streamlit
├── .env # Variáveis sensíveis (não versionado)
├── .gitignore # Arquivos ignorados no versionamento
├── requirements.txt # Bibliotecas do projeto
│
├── consultas/
│ └── total_vendas.py # Consulta do total de vendas no período
│
└── database/
└── conexao.py # Função de conexão com o banco Firebird


## 🛠️ Como Executar Localmente

1. Clone o repositório:

  git clone https://github.com/LarissaCordovil/Painel_Vendas_Mercado.git
  cd Painel_Vendas_Mercado

2. Instale as dependências:

  pip install -r requirements.txt

3. Crie um arquivo .env com suas configurações:
   
FIREBIRD_PATH=CAMINHO/DO/SEU/fbclient.dll
FIREBIRD_DSN=localhost:C:/caminho/para/seu/arquivo.FDB
FIREBIRD_USER=SEU_USUARIO
FIREBIRD_PASSWORD=SUA_SENHA

4. Execute o painel com streamlit:
 
  streamlit run app.py



