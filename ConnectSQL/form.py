import streamlit as st
import dados

st.title("Cadastro de Funcionarios")

nome = st.text_input("Nome do funcionario:")
sobrenome = st.text_input("Sobrenome do funcionario:")
idade = st.number_input("Idade do funcionario:", min_value=0, max_value= 120, step=1)

if st.button('Adicionar'):
    dados.insere_dados(nome, sobrenome, idade)
    st.success("Funcionario adicionado com sucesso!")
    
funcionarios = dados.obter_dados()
st.header("Lista de Funcionarios")
st.table(funcionarios)